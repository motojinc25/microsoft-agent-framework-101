# https://learn.microsoft.com/en-us/agent-framework/agents/running-agents?pivots=programming-language-python
# Create and run an agent with Agent Framework, Azure OpenAI Chat Completion service
# Environment variables
#   - AZURE_OPENAI_ENDPOINT
#   - AZURE_OPENAI_CHAT_DEPLOYMENT_NAME

import asyncio

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

    # Running the agent
    result = await agent.run("日本語で面白いジョークを教えてください。")
    print(result.text)


if __name__ == "__main__":
    asyncio.run(main())

# Expected output:
# もちろん！では、こちらをどうぞ：
#
# カタツムリがスピード違反で捕まったんだって。警察官が理由を聞いたら、カタツムリはこう言ったんだ。「もっとゆっくり走ってたら、家に忘れ物しちゃってた！」
