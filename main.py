from claude_agent_sdk import ClaudeSDKClient, AssistantMessage, TextBlock, ClaudeAgentOptions
import asyncio

SYSTEM_PROMPT = """
Você é um professor de Python especializado em ensinar desenvolvedores Java.

Seu aluno já tem experiência sólida em Java e Spring Boot. Seu papel é transferir esse conhecimento para Python — nunca ensinar do zero, mas sempre fazer a ponte entre o que ele já sabe e o que está aprendendo.

Regras:
- Sempre que explicar um conceito Python, mostre o equivalente em Java logo em seguida
- Use o formato: "Em Python: [conceito] | Em Java: [equivalente]"
- Seja didático e encorajador — o aluno está aprendendo sozinho
- Quando o aluno errar, dê pistas, não a resposta direta
- Prefira exemplos práticos a definições teóricas
- Se o aluno perguntar algo fora de Python, redirecione gentilmente
- Para conceitos complexos, explique primeiro o problema que o conceito resolve antes de mostrar o código
"""

async def main():
    opcoes = ClaudeAgentOptions(system_prompt=SYSTEM_PROMPT,
                                max_budget_usd=2.0)
    async with ClaudeSDKClient(options=opcoes) as client:
        while True:
            pergunta = input("Você: ")
            print()

            if not pergunta:
                print("Você precisa enviar alguma mensagem.")
                print()
                continue

            if pergunta.lower() == "sair":
                break

            print("-=" * 40)

            await client.query(pergunta)

            async for mensagem in client.receive_response():
                if isinstance(mensagem, AssistantMessage):
                    for bloco in mensagem.content:
                        if isinstance(bloco, TextBlock):
                            print(f"Professor: {bloco.text}")
                            print()
                            print("-=" * 40)


asyncio.run(main())
