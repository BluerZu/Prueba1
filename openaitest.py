import openai
from pydantic import BaseModel

class Document(BaseModel):
    prompt: str = ''

def inference(prompt: str) -> list:
    openai.organization = 'org-DYRwCOZ92Bsf4lIsYceu2SVQ'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))
    print(prompt)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = 1,
        messages=[
            {"role": "system", "content": """Eres una base de datos enorme, que contiene toda la información histórica de la
            humanidad, cuando se te envíe una fecha, responderás con un dato histórico relevante que haya ocurrido en dicha fecha.
            E.G.
            10 de agosto
            Dato relevante: Día de la Independencia de Quito
            """},
            {"role": "user", "content": prompt}
        ],
        max_tokens = 50
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print("Se han utilizado los siguientes tokens: " + str(total_tokens))
    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]

