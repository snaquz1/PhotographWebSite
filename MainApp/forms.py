from django import forms


class RequestForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя', widget=forms.TextInput(
        attrs={"placeholder": "Ваше имя", "class": "nameinput input"}))

    phone = forms.CharField(max_length=100, label='Телефон', initial="7", required=True, widget=forms.TextInput(
        attrs={"placeholder": "Ваш номер телефона", "class": "phoneinput input"}))

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя', widget=forms.TextInput(
        attrs={"placeholder": "Ваше имя", "class": "nameinput input"}))

    rate = forms.IntegerField(required=True, label='Оценка', widget=forms.NumberInput(
        attrs={"class": "rateinput input"}),
        min_value=1, max_value=5)

    text = forms.CharField(max_length=1000, required=True, label='Текст', widget=forms.Textarea(
        attrs={"placeholder": "Ваш отзыв", "class": "textinput input"}))

