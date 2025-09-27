## uv init

## uv add langchain langchain-openai black python-dotenv

# High-Level Steps to Arrive at the Final Answer

1. **Environment Setup**
   - Loads environment variables using `dotenv` for API keys and configuration.

2. **Tool Definition**
   - Imports and registers available tools (e.g., `get_text_length`) for the agent to use.

3. **Prompt Preparation**
   - Loads a custom prompt template (`REACT_PROMPT_TEMPLATE`) describing the agent's reasoning and tool usage format.
   - Renders tool descriptions and names into the prompt.

4. **LLM Initialization**
   - Initializes the ChatOpenAI LLM with specific parameters and attaches a callback handler for logging.

5. **Agent Construction**
   - Chains together input mapping, prompt formatting, LLM invocation, and output parsing using the ReAct pattern.

6. **Agent Execution Loop**
   - Repeatedly invokes the agent with the input question and accumulated intermediate steps.
   - If the agent decides to use a tool, finds the tool by name and executes it with the provided input.
   - Logs the observation and appends it to the intermediate steps.

7. **Final Answer Extraction**
   - When the agent reaches a final answer, prints the result.

## Example Question

- "What is the length of 'DOG' in characters?"

The agent reasons step-by-step, uses the registered tool to compute the answer, and outputs the final result.