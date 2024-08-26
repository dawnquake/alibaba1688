from django.shortcuts import render
from .forms import InputForm
from alibaba1688api.main import returnKeywordAndDetails
import os

LOCAL = os.getenv('LOCAL')

# Create your views here.
def process_input(keyWord, beginPage, pageSize):

    if LOCAL == '1':
        result = returnKeywordAndDetails(keyWord, beginPage, pageSize)
    elif LOCAL == '0':
        result = keyWord + beginPage + pageSize

    return result

def index(request):

    result = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            keyWord = str(form.cleaned_data['keyWord'])
            beginPage = str(form.cleaned_data['beginPage'])
            pageSize = str(form.cleaned_data['pageSize'])

            result = process_input(keyWord, beginPage, pageSize)
    else:
        form = InputForm()


    return render(request, 'homepage/index.html', {'form': form, 'result': result})
