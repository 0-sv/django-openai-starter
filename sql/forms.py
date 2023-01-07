import openai
from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='question', max_length=100)

    def ask_openai(self, question):
        response = openai.Completion.create(model="text-curie-001",
                                            prompt=question,
                                            temperature=0,
                                            max_tokens=7)
        return response['choices'][0]['text']
