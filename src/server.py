from fastapi import FastAPI
from typing import List

from src.models import Question, Choice, Choices

app = FastAPI(
    title='ETH-MATRIC Question Service',
    description='Service for grabbing question related data.')

@app.get('/question/{question_id}', response_model=Question, tags=['Question'])
def get_question(question_id: int) -> Question:
    return Question(**{
        'id': question_id,
        'question': 'This is an example ________.'
    })

@app.get('/choices/{question_id}', response_model=Choices, tags=['Answer'])
def get_choices(question_id: int) -> Choices:
    return Choices(**{
        'choices': [
            Choice(**{
                'id': i,
                'description': f'choice{i}'
            }) for i in range(1, 4)
        ]})
