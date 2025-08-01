import os
from dotenv import load_dotenv
import chainlit as cl
import requests

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, RunConfig

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is set
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")

# Setup Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Setup model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Run configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define the tool function
@function_tool
def get_crypto_price(symbol: str) -> str:
    """
    Fetch current price of given cryptocurrency symbol from Binance.
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f"The current price of {symbol.upper()} is {data['price']} USDT."
    else:
        return f"❌ Failed to fetch price for {symbol.upper()}. Please check the symbol and try again."

# Define the agent
CryptoCurrency = Agent(
    name="Crypto Agent",
    instructions="You are a cryptocurrency expert. Use the get_crypto_price function to provide real-time prices of coins like BTC and ETH.",
    tools=[get_crypto_price]
)

# Chainlit entry point

@cl.on_message
async def main(message: cl.Message):
    response = await Runner.run(
        CryptoCurrency,
        input=message.content,
        run_config=config
    )

    if response and response.final_output:
        await cl.Message(content=response.final_output).send()
    else:
        await cl.Message(content="⚠️ Sorry, I couldn't fetch a valid response.").send()