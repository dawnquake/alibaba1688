from django.shortcuts import render
from .forms import InputForm
import requests

# Create your views here.

def process_input(keyWord):

    result = keyWord.upper()
    # API endpoint
    url = "https://api.coinbase.com/v2/currencies"

    # Send a GET request to the API
    response = requests.get(url)

    print(response)

    result = response.json()

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
