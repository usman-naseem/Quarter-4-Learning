from agents import Agent, Runner, input_guardrail ,GuardrailFunctionOutput,TResponseInputItem,InputGuardrailTripwireTriggered
from connection import config
import rich
from pydantic import BaseModel
import asyncio
from dotenv import load_dotenv

load_dotenv(".env")

class TeacherResponse(BaseModel):
    message: str
    isOffTopic: bool

@input_guardrail
async def teacher_guardrail(ctx, agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    # Manually check if user input is emotional or off-topic
    if isinstance(input, list):
        user_input = input[0].text
    else:
        user_input = input

    is_off_topic = "change my class timings" in user_input.lower() or "😭" in user_input

    response = TeacherResponse(
        message="Please stay focused on academic topics.",
        isOffTopic=is_off_topic,
    )

    rich.print(response)

    return GuardrailFunctionOutput(
        output_info=response,
        tripwire_triggered=is_off_topic,
    )

# Define the agent
teacher_agent = Agent(
    name="Teacher Agent",
    instructions="You are a helpful assitant",
    input_guardrails=[teacher_guardrail]
)

# Main function to run the test
async def main():
    try:
        result = await Runner.run(
            teacher_agent,
            "I want to change my class timings 😭😭",
            run_config=config,
        )
        rich.print(result.final_output)
    except InputGuardrailTripwireTriggered:
        
        print("⚠️Please speak to the administration regarding timing changes.")

if __name__ == "__main__":
    asyncio.run(main())
