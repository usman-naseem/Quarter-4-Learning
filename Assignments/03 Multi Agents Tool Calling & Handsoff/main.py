from agents import Agent, Runner, trace, function_tool
from connection import config

from dotenv import load_dotenv
# import rich
load_dotenv(".env")

@function_tool
def get_current_Location():
    return"Karachi"
@function_tool
def  get_breaking_news():
    return"The stock market is up today!"

plantagenet = Agent(
    name="plantagenet",
    instructions="You are a plant agent that provides information about plants.",
    model='gpt3'
)
parentagent = Agent(
    name="parentagent",
    instructions="You are a sub-agent that can answer questions about weather, location, and news and photosynthesis and handsoffs.",
    tools=[get_current_Location , get_breaking_news],
    handoffs=[plantagenet]
)
result = Runner.run_sync(
    parentagent,
    """ 
        1. What is my current location?
        3. Any breaking news?
        2. What is photosynthesis
    """,
    run_config=config
)
# print('='*50)
# print("Result: ",result.last_agent.name)
# rich.print(result.new_items)
print("Result: ",result.final_output)
