# Tool Calling in OpenAI Agents SDK

## What Is Tool Calling?

In the OpenAI Agents SDK, **tool calling** refers to the process where an AI agent—powered by a language model—detects that it needs to perform a specific task (like fetching data, executing code, or searching the web) and then **calls an external tool** (essentially a function or service) to fulfill that task. It’s how your agent goes from just “talking” to actually “doing.” ([Medium][1], [OpenAI GitHub Pages][2])

## How It Works

There are three main types of tools in the SDK:

1. **Hosted tools** – Built-in tools that run on OpenAI's servers, such as:
   - WebSearchTool
   - FileSearchTool
   - CodeInterpreterTool
   - ImageGenerationTool  
     ([Sid Bharath][3], [OpenAI GitHub Pages][2])

2. **Function tools** – Any Python function you define can automatically become a callable tool. The SDK wraps it, extracting its signature and docstring to generate input schemas and metadata. ([OpenAI GitHub Pages][2])

3. **Agents as tools** – You can even treat other agents as callable tools, enabling hierarchical or collaborative workflows without fully handing off control. ([OpenAI GitHub Pages][2])

## Tool Calling vs. Function Calling

- **Tool calling** is the conceptual step—when the agent identifies the need to perform a task using a tool.
- **Function calling** is the actual code execution—running that tool (function), passing the necessary arguments, and collecting the response. ([Medium][4])

## Developer Workflow Example

1. **Define a tool** (e.g., a weather function):

   ```python
   @function_tool
   def get_weather(city: str) -> str:
       """Returns current weather for a city."""
       return f"Weather in {city} is sunny, 30°C"


