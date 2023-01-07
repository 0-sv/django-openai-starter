import logging

import openai
from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='question', max_length=100)

    def ask_openai(self):
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=self.cleaned_data['question'],
                                            temperature=0,
                                            max_tokens=20)
        logging.info(response)
        return response['choices'][0]['text']
