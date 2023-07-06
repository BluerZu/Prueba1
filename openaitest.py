import openai
from pydantic import BaseModel




class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    openai.organization = 'org-DYRwCOZ92Bsf4lIsYceu2SVQ'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un gran historiador, que me va a dar un dato relevante que haya pasado en la historia, de acuerdo.
            a la fecha que se te envíe.
            E.G
            10 de Agosto
            Dato relevante en la historia:
            Primer grito de la independencia de Quito.
            """},
            {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print("Se han utilizado los siguientes tokens: " + total_tokens)
    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]

