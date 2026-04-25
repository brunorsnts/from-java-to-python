from fastapi import APIRouter, Request
from pydantic import BaseModel
from services.agent_service import enviar_mensagem_para_agente

class MensagemRequest(BaseModel):
    pergunta: str

router = APIRouter()

@router.post("/chat")
async def recebeMensage(request: Request, body: MensagemRequest):
    client = request.app.state.client
    resposta = await enviar_mensagem_para_agente(client, body.pergunta)
    return {"resposta": resposta}