from django import forms

# creating a form
class InputForm(forms.Form):
    keyWord = forms.CharField(label="输入需要搜索的关键词")