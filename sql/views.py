from django.shortcuts import render

from .forms import QuestionForm


def index(request):
    output = "waiting for input"
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            output = form.ask_openai()
    else:
        form = QuestionForm()
    return render(request, 'sql/poc.html', {'form': form, 'output': output})
