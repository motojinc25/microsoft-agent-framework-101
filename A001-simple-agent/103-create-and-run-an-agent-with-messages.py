# https://learn.microsoft.com/en-us/agent-framework/agents/running-agents?pivots=programming-language-python
# Create and run an agent with Agent Framework, Azure OpenAI Chat Completion service
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
    agent = AzureOpenAIChatClient(
        credential=AzureCliCredential(),
    ).as_agent(instructions="You are good at telling jokes.", name="Joker")

    # Running the agent with a ChatMessage
    message = Message(
        role="user",
        contents=[
            Content.from_text(text="画像の意味についてジョークを言ってください。"),
            Content.from_uri(
                uri="https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/RWCZER-Legal-IP-Trademarks-CP-MS-logo-740x417-1",
                media_type="image/jpeg",
            ),
        ],
    )
    result = await agent.run(message)
    print(result.text)


if __name__ == "__main__":
    asyncio.run(main())

# Expected output:
# これを見て思ったんですが、コンピューターが寒がる時ってどうするんでしょう？
# 「マイクロソフト（マイク・ロソフト）で温めるんですよ！」（寒かったらすみません！）
