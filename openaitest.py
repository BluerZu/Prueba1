import openai
from pydantic import BaseModel

openai.organization = 'org-Cbvcdr6eNau56Sbr39n9QGvY'
openai.api_key = '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'


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = 0.9,
        context = "Estas en un aula de clases",
        messages=[
          {"role": "system", "content": """Eres un contador de letras de las palabras que te envíen""",
           },
          {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print("Se han utilizado los siguientes tokens: " + total_tokens)
    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]

