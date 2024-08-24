from django.shortcuts import render
from .forms import InputForm
from alibaba1688api.main import returnKeywordAndDetails

# Create your views here.

def process_input(keyWord):

    result = returnKeywordAndDetails(keyWord)

    return result

def index(request):

    result = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['keyWord']
            result = process_input(user_input)
    else:
        form = InputForm()


    return render(request, 'homepage/index.html', {'form': form, 'result': result})
