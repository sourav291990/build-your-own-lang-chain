from typing import List, Union
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain_openai import ChatOpenAI
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain.schema import AgentAction, AgentFinish
from langchain.tools import Tool
from langchain.agents.format_scratchpad import format_log_to_str
from callbacks import AgentCallbackHandler
from promts.prompt import REACT_PROMPT_TEMPLATE
from tools.tools import get_text_length

load_dotenv()

def find_tool_by_name(tools: List[Tool], name: str):
    for tool in tools:
        if tool.name == name:
            return tool
    return ValueError(f"Tool with name {name} not found.")


def main():
    tools = [get_text_length]
    template = REACT_PROMPT_TEMPLATE

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools=tools),
        tool_names=", ".join([tool.name for tool in tools]),
    )

    llm = ChatOpenAI(
        temperature=0,
        model_kwargs={"stop": ["Observation", "\nObservation"]},
        callbacks=[AgentCallbackHandler()],
    )

    intermediate_steps = []
    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"]),
        }
        | prompt
        | llm
        | ReActSingleInputOutputParser()
    )

    
    agent_step = ""
    while not isinstance(agent_step, AgentFinish):
        agent_step: Union[AgentAction, AgentFinish] = agent.invoke(
            {
                "input": "What is the length of 'DOG' in characters?",
                "agent_scratchpad": intermediate_steps,
            }
        )

        if isinstance(agent_step, AgentAction):
            tool_name = agent_step.tool
            tool_to_use = find_tool_by_name(tools, tool_name)
            tool_input = agent_step.tool_input
            observation = tool_to_use.func(str(tool_input))
            print(f"Observation: {observation}")

            intermediate_steps.append((agent_step, str(observation)))

    if isinstance(agent_step, AgentFinish):
        print(f"Final Answer: {agent_step.return_values}")


if __name__ == "__main__":
    main()
