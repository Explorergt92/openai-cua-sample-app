# Copyright (c) 2025 Eloquent-Algorithmics LLC
# All rights reserved.

"""Example shows how to use the ScrapybaraBrowser with custom functions."""

from agent import Agent
from computers import ScrapybaraBrowser

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Determine weather in my location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["c", "f"]},
            },
            "additionalProperties": False,
            "required": ["location", "unit"],
        },
    },
]


def main() -> None:
    """Run the main application loop for the ScrapybaraBrowser example."""
    with ScrapybaraBrowser() as computer:
        agent = Agent(tools=tools, computer=computer)
        items = []
        while True:
            user_input = input("> ")
            items.append({"role": "user", "content": user_input})
            output_items = agent.run_full_turn(items)
            items += output_items


if __name__ == "__main__":
    main()
