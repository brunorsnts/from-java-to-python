# from-java-to-python

Agente conversacional que funciona como um professor de Python especializado em desenvolvedores Java. Você digita um conceito Python, ele explica com o equivalente em Java do lado — transferindo o conhecimento que você já tem para a nova linguagem.

## Por que esse projeto existe

Tenho base sólida em Java e Spring Boot e estou aprendendo Python. Em vez de começar do zero, quis aproveitar o que já sei: cada conceito Python é explicado com a analogia Java correspondente, acelerando o aprendizado pela transferência de conhecimento.

O projeto nasceu também como exercício prático para aprender o **Claude Agent SDK** da Anthropic — construindo algo útil para o meu próprio estudo.

## Tecnologias

| Tecnologia | Função |
|---|---|
| Python 3.13 | Linguagem do projeto |
| [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) | SDK para criação do agente |
| FastAPI + uvicorn | Interface web e servidor ASGI |
| Anthropic API | Modelo de IA (Claude) |
| pip | Gerenciamento de dependências |

## Pré-requisitos

- Python 3.10 ou superior
- Conta na [Anthropic Console](https://console.anthropic.com/) com uma API key

## Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/brunorsnts/from-java-to-python.git
cd from-java-to-python
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure a API key**

Crie um arquivo `.env` na raiz (use o `.env.example` como modelo):
```
ANTHROPIC_API_KEY=sua_chave_aqui
```

Ou configure como variável de ambiente do sistema.

**5. Execute o agente**

Versão terminal:
```bash
python main.py
```

Versão web:
```bash
uvicorn app:app --reload
```

Acesse `http://127.0.0.1:8000` no browser.

## Como usar

**Terminal:** após iniciar, o terminal fica aguardando sua pergunta:

```
Você: Como funcionam as listas em Python?
Professor: Em Python, listas são como ArrayList do Java...
```

Para encerrar, digite `sair`.

**Web:** acesse `http://127.0.0.1:8000`, digite sua pergunta no campo e envie.

## Aprendizados

Projeto construído durante estudos de Python e Claude Agent SDK. Cada linha do `main.py` foi escrita com entendimento — sem copiar/colar código pronto.
