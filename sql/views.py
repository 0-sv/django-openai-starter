from django.shortcuts import render

from .forms import QuestionForm


def index(request):
    form = QuestionForm()
    return render(request, 'sql/poc.html', {'form': form})
