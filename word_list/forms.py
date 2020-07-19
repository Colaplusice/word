from django import forms

from word_list.models import User


class UploadFileForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control required'}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'required'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).first() is None:
            raise forms.ValidationError("user not found")

    # def clean_file(self):
    #     file = self.cleaned_data.get('file')
    #     print('file_name', file)
    #     if not file.endswith('.txt'):
    #         raise forms.ValidationError("file type must be text")
