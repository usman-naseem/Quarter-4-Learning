
# 🧠Tool Calling in OpenAI Agents SDK

Tool Calling allows OpenAI models like GPT-4 or GPT-4o to **autonomously use your custom functions**. It's a key feature for building smart applications where the AI can access APIs, files, databases, or generate content like this! 

---

## ⚙️ How Tool Calling Works

1. **Define your Python function** (e.g., `generate_readme`)
2. **Register it as a tool** using a schema
3. **GPT decides** when and how to use it
4. The tool is executed and its result is returned to the conversation

---

## ✅ Example Use Case

User prompt:
> "Create a README.md file for an LLM project."

The model calls:
```python
generate_readme()

