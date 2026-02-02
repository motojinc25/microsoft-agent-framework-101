# https://learn.microsoft.com/en-us/agent-framework/tutorials/agents/images?pivots=programming-language-python
# Using images with an agent, Azure OpenAI Chat Completion service
# Environment variables
#   - AZURE_OPENAI_ENDPOINT
#   - AZURE_OPENAI_CHAT_DEPLOYMENT_NAME

import asyncio

from agent_framework import ChatMessage, Role, TextContent, UriContent
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential


async def main():
    # Create an agent
    agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent(
        instructions="You are a helpful agent that can analyze images", name="VisionAgent"
    )

    # Load image from URI
    message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="何のイメージですか？"),
            UriContent(
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
