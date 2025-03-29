from django import forms


class RequestForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя', widget=forms.TextInput(
        attrs={"placeholder": "Ваше имя", "class": "nameinput input"}))

    phone = forms.CharField(max_length=100, label='Телефон', initial="7", required=True, widget=forms.TextInput(
        attrs={"placeholder": "Ваш номер телефона", "class": "phoneinput input"}))

        