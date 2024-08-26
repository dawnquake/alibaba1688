from django import forms

# creating a form
class InputForm(forms.Form):
    keyWord = forms.CharField(label="输入需要搜索的关键词(不能为空)", required=True)
    beginPage = forms.IntegerField(label="输入需要搜索的页数(至少1)", min_value = 1)
    pageSize = forms.IntegerField(label="输入需要搜索的每页数量(至少1,最多50)", min_value = 1, max_value=50)