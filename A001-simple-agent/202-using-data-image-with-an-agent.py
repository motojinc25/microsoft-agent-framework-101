# https://learn.microsoft.com/en-us/agent-framework/agents/multimodal?pivots=programming-language-python
# Using images with an agent, Azure OpenAI Chat Completion service
# Environment variables
#   - AZURE_OPENAI_ENDPOINT
#   - AZURE_OPENAI_CHAT_DEPLOYMENT_NAME

import asyncio
from pathlib import Path

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

    # Load image from local file
    image_path = Path(__file__).parent / "assets" / "image-fujisan.png"
    with image_path.open("rb") as f:
        image_bytes = f.read()

    message = Message(
        role="user",
        contents=[
            Content.from_text(text="何のイメージですか？"),
            Content.from_data(data=image_bytes, media_type="image/png"),
        ],
    )

    # Running the agent
    result = await agent.run(message)
    print(result.text)


if __name__ == "__main__":
    asyncio.run(main())

# Expected output:
# この画像は、富士山とその反射が湖に映っている風景です。桜や木々が湖畔に広がっていて、夕焼けの空が鮮やかです。この美しい自然の景観は日本を代表する象徴的なシーンの一つです。
