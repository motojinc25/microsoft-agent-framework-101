# https://learn.microsoft.com/en-us/agent-framework/agents/multimodal?pivots=programming-language-python
# Using images with an agent, Azure OpenAI Chat Completion service
# Environment variables
#   - AZURE_OPENAI_ENDPOINT
#   - AZURE_OPENAI_CHAT_DEPLOYMENT_NAME

import asyncio

from agent_framework import Content, Message
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


async def main():
    # Create an agent
    agent = AzureOpenAIChatClient(credential=AzureCliCredential()).as_agent(
        instructions="You are a helpful agent that can analyze images", name="VisionAgent"
    )

    # Load image from URI
    message = Message(
        role="user",
        contents=[
            Content.from_text(text="何のイメージですか？"),
            Content.from_uri(
                uri="https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/RWCZER-Legal-IP-Trademarks-CP-MS-logo-740x417-1",
                media_type="image/jpeg",
            ),
        ],
    )

    # Running the agent
    result = await agent.run(message)
    print(result.text)


if __name__ == "__main__":
    asyncio.run(main())

# Expected output:
# これはMicrosoftのロゴです。Microsoftは、ソフトウェア、コンピュータハードウェア、クラウドサービスなどを提供するアメリカの大手技術企業です。
