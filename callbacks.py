from langchain.callbacks.base import BaseCallbackHandler


class AgentCallbackHandler(BaseCallbackHandler):
    """Callback handler for agent execution."""

    def on_llm_start(
        self,
        serialized,
        prompts,
        *,
        run_id,
        parent_run_id=None,
        tags=None,
        metadata=None,
        **kwargs,
    ):
        print("******Prompts******")
        print("LLM starting with prompts:", prompts)

    def on_llm_end(self, response, *, run_id, parent_run_id=None, **kwargs):
        print("******Response******")
        print("LLM ended with response:", response)
