from langchain.agents import tool



@tool
def get_text_length(text: str) -> int:
    """Returns the length of the given text."""
    print(f"Calculating length of text: {text}")
    return len(text)