from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 🚀 Cargar modelo HRM desde Hugging Face
MODEL_NAME = "ruta/del/modelo-en-huggingface"  # <-- Cambia por el nombre exacto del modelo HRM
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

app = FastAPI()

class ReasonRequest(BaseModel):
    context: str
    question: str

@app.post("/reason")
async def reason(req: ReasonRequest):
    prompt = f"Contexto:\n{req.context}\n\nPregunta:\n{req.question}\n\nRazonamiento paso a paso:"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=300)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"plan": "Razonamiento generado", "answerDraft": response_text}

