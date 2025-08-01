from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import asyncio
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

# Setup external OpenAI client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Model and config
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Lyric Poetry
Lyric_poetry = Agent(
    name="Lyric Poetry",
    instructions="You are a lyric poetry analyst agent. Analyze lyric poems and explain their meaning (tashree)",)

Narrative_poetry = Agent(
    name="Narrative Poetry",
    instructions="'You are a narrative poetry analyst agent. Analyze narrative poems and explain their meaning (tashree)"
)

Dramatic_poetry = Agent(
    name="Dramatic Poetry",
    instructions="You are a dramatic poetry analyst agent. Analyze dramatic poems and explain their meaning (tashree)"
)
Triage_Agent = Agent(
    name="Triage Agent",
    instructions="""
You are a poetry analysis expert. Given any Urdu or English poem, first identify its type:
- If it's emotional/personal, it's Lyric Poetry.
- If it tells a story, it's Narrative Poetry.
- If it's written for performance or has dialogue, it's Dramatic Poetry.

 
 write a long, detailed tashree (10+ lines) in Simple English. 

""",
handoffs=[Dramatic_poetry,Lyric_poetry,Narrative_poetry]
)


# ✅ Basic Runner (no config here)
runner = Runner()

# Async main function
async def main():
    poems = [
        {
            "type": "Narrative",
            "text": """
John walked through the burning town,
Where smoke rose high and ash fell down.
He saved a child with trembling hands,
Then vanished into distant lands.
            """
        },
        {
            "type": "Lyric",
            "text": """
In the quiet of night, I sit and cry,
Thinking of moments that fluttered by.
My heart speaks in silent rhyme,
Wishing to turn back time.
            """
        },
        {
            "type": "Dramatic",
            "text": """
(To the audience)  
Why must I suffer this endless pain?  
Is fate not cruel enough already?  
I begged the stars for mercy, in vain,  
And now, alone, I speak to thee.
            """
        }
    ]

    for poem in poems:
        print(f"🎭 Poem Type (for reference): {poem['type']}")
        print("🎤 Input Poem:")
        print(poem["text"])
        print("\n🧠 Analyzing and getting tashree...\n")

        # ✅ ONLY pass agent and input text
        response = await runner.run(
            Triage_Agent,
            poem["text"],
            run_config=config
        )

        print("📜 Tashree (Explanation):")
        print(response.final_output)
        print("\n" + "—" * 60 + "\n")


# Run main
asyncio.run(main())



# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# import asyncio
# import os
# from dotenv import load_dotenv

# # Load .env
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set in .env")

# # External Client
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# # Model and Config
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # Define Poetry Agents
# Lyric_poetry = Agent(
#     name="Lyric Poetry",
#     instructions="You are an expert in Lyric Poetry. Give a long and detailed explanation (tashree) of the poem using simple English. Focus on emotions, feelings, and personal themes."
# )

# Narrative_poetry = Agent(
#     name="Narrative Poetry",
#     instructions="You are an expert in Narrative Poetry. Give a long and detailed explanation (tashree) of the poem using simple English. Focus on story, plot, and events."
# )

# Dramatic_poetry = Agent(
#     name="Dramatic Poetry",
#     instructions="You are an expert in Dramatic Poetry. Give a long and detailed explanation (tashree) of the poem using simple English. Focus on performance, dialogue, and character."
# )

# Triage_Agent = Agent(
#     name="Triage Agent",
#     instructions="""
# You are a poetry expert. First, identify what type of poem this is:
# - Lyric (emotional/personal)
# - Narrative (tells a story)
# - Dramatic (for performance, has dialogue)

# Then, write a long detailed tashree (10+ lines) in simple English 
# """
# )

# # Runner
# runner = Runner()

# # List of poems
# poems = [
#     {
#         "title": "Lyric Poem",
#         "text": """
# In the quiet of night, I sit and cry,
# Thinking of moments that fluttered by.
# My heart speaks in silent rhyme,
# Wishing to turn back time.
#         """
#     },
#     {
#         "title": "Narrative Poem",
#         "text": """
# John walked through the burning town,
# Where smoke rose high and ash fell down.
# He saved a child with trembling hands,
# Then vanished into distant lands.
#         """
#     },
#     {
#         "title": "Dramatic Poem",
#         "text": """
# CHARLES: Why do you weep, Maria?
# MARIA: The night hides truths I cannot speak.
# CHARLES: Then let the stars bear witness, love—
# That I shall stand with you till dawn.
#         """
#     }
# ]

# # Function to run agents for each poem
# async def analyze_poem(poem_input):
#     triage_result = await runner.run(Triage_Agent, poem_input, run_config=config)
#     lyric_result = await runner.run(Lyric_poetry, poem_input, run_config=config)
#     narrative_result = await runner.run(Narrative_poetry, poem_input, run_config=config)
#     dramatic_result = await runner.run(Dramatic_poetry, poem_input, run_config=config)

#     print("\n🧠 Triage Agent Tashree:\n")
#     print(triage_result.final_output)

#     print("\n📜 Lyric Poetry Tashree:\n")
#     print(lyric_result.final_output)

#     print("\n📜 Narrative Poetry Tashree:\n")
#     print(narrative_result.final_output)

#     print("\n📜 Dramatic Poetry Tashree:\n")
#     print(dramatic_result.final_output)

# # Run all poems
# async def main():
#     for poem in poems:
#         await analyze_poem(poem["text"])

# # Execute
# asyncio.run(main())
