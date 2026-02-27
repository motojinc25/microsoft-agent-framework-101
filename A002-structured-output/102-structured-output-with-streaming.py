# https://learn.microsoft.com/en-us/agent-framework/agents/structured-output?pivots=programming-language-python
# Producing Structured Output with Agents, Azure OpenAI Chat Completion service
# Environment variables
#   - AZURE_OPENAI_ENDPOINT
#   - AZURE_OPENAI_CHAT_DEPLOYMENT_NAME

import asyncio

from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()


# Define a Pydantic model that represents the structure of the output
class PersonInfo(BaseModel):
    """Information about a person."""

    name: str | None = None
    age: int | None = None
    occupation: str | None = None


async def main():
    # Create an agent
    agent = AzureOpenAIChatClient(
        credential=AzureCliCredential(),
    ).as_agent(instructions="You are a helpful assistant that extracts person information from text.", name="Assistant")

    # Running the agent
    stream = agent.run(
        "Please provide information about John Smith, who is a 35-year-old software engineer.",
        stream=True,
        options={"response_format": PersonInfo},
    )
    final_response = await stream.get_final_response()
    if final_response.value:
        person_info = final_response.value
        print(f"Name: {person_info.name}, Age: {person_info.age}, Occupation: {person_info.occupation}")
    else:
        print("No structured data found in response")


if __name__ == "__main__":
    asyncio.run(main())

# Expected output:
# Name: John Smith, Age: 35, Occupation: software engineer
