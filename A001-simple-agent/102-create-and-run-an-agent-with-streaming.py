# https://learn.microsoft.com/en-us/agent-framework/tutorials/agents/run-agent?pivots=programming-language-python
# Create and run an agent with Agent Framework, Azure OpenAI Chat Completion service
# Environment variables
#   - AZURE_OPENAI_ENDPOINT
#   - AZURE_OPENAI_CHAT_DEPLOYMENT_NAME

import asyncio

from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential


async def main():
    # Create an agent
    agent = AzureOpenAIChatClient(
        credential=AzureCliCredential(),
    ).create_agent(instructions="You are good at telling jokes.", name="Joker")

    # Running the agent with streaming
    async for update in agent.run_stream("日本語で面白いジョークをA4用紙1枚分で教えてください。"):
        if update.text:
            print(update.text, end="", flush=True)
    print()  # New line after streaming is complete


if __name__ == "__main__":
    asyncio.run(main())

# Expected output:
# もちろん、日本語でジョークをお届けします！A4用紙1枚分には少し足りないかもしれませんが、楽しんでいただければ幸いです。
#
# ---
#
# ある日、タヌキが森の中で他の動物たちに集合をかけました。「ねえみんな、面白いゲームを思いついたんだ。『動物しりとり』をしようよ！」
#
# ウサギが興味津々で、「どうやってするの？」と聞きました。
#
# 「簡単だよ。しりとりの要領で動物の名前を言えばいいんだ。ただし、最後に『リ』で終わる動物の名前を言ったら負けね！」とタヌキが説明しました。
#
# 早速ゲームが始まりました。最初はウサギが「ウサギ」と言い、それを受けてカメが「ギャルドック」と返しました。
#
# その後、イヌが「クワガタ」と言い、サルが「タヌキ」と返しました。タヌキはニヤリとして、「キツネ」と言いました。
#
# ここでキジが、ちょっと悩んでから「ゼブラ」と言いました。
#
# ウサギが「ライオン！」と叫ぶと、その次にタヌキに順番が回ってきました。
#
# タヌキは少し考えて、「ン・・・ダルマ！」と突然叫びました。
#
# みんなが「それ、動物じゃないよ！」と笑いつつ抗議しましたが、タヌキは開き直って、「まぁ、次回は動物縛りじゃなくてタヌキのルールでやろうよ！」と言いながら、おおいに盛り上がりました。
#
# ---
#
# ジョークの内容が多すぎてA4用紙に収まりきらない時にも、簡潔に楽しめるジョークがあるのはありがたいですね。それでは、また別の機会に！
