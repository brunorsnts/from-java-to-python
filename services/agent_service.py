from claude_agent_sdk import ClaudeSDKClient, AssistantMessage, TextBlock, ClaudeAgentOptions

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

def criar_cliente():
    opcoes = ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        max_budget_usd=2.0,
        model="claude-sonnet-4-6"
    )
    return ClaudeSDKClient(options=opcoes)
    

async def enviar_mensagem_para_agente(client, pergunta):
    await client.query(pergunta)

    resposta = ""
    async for mensagem in client.receive_response():
                if isinstance(mensagem, AssistantMessage):
                    for bloco in mensagem.content:
                        if isinstance(bloco, TextBlock):
                            resposta += bloco.text
    return resposta
        

