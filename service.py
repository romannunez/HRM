from fastapi import FastAPI
from pydantic import BaseModel

# 🔹 Importar el modelo HRM desde el repo que clonaste
# Ejemplo: from hrm import HRMModel
# Ajustá esta línea según cómo se carga el modelo en tu repo
# hrm_model = HRMModel.load("ruta_o_configuracion")

app = FastAPI()

class ReasonRequest(BaseModel):
    context: str
    question: str

@app.post("/reason")
async def reason(req: ReasonRequest):
    context = req.context
    question = req.question

    # 🔹 Aquí llamamos a HRM para obtener el razonamiento
    # Esto depende de cómo funciona la API del modelo en tu repo
    # Ejemplo ficticio:
    # reasoning = hrm_model.reason(context, question)
    # return {"plan": reasoning.plan, "steps": reasoning.steps, "answerDraft": reasoning.draft}

    # 🔹 Por ahora, si no sabes cómo invocar, ponemos un mock
    return {
        "plan": f"Analizar contexto y responder a '{question}'",
        "steps": ["Analizar contexto", "Generar respuesta"],
        "answerDraft": f"Respuesta provisional para: {question}"
    }
