import os
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model


def create_travel_agent(config):
    if 'OPENAI_API_KEY' not in os.environ or not os.environ['OPENAI_API_KEY']:
        os.environ['OPENAI_API_KEY'] = config['api_key']
    model = init_chat_model(
        model=config['model'],
        model_provider='openai',
        base_url=config['base_url'],
        temperature=0,
        verbose=config['verbose'],
    )
    tools = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": []}
                }
            }
        }
    ]
    agent = create_agent(
        model=model,
        # tools=tools,
    )
    return agent
