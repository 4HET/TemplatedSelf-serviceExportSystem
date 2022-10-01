from django import forms


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    title = "admin"
    file = forms.FileField()

# 多个文件上传
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))