from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='称呼', max_length=20, error_messages={
        'required': '请填写称呼',
        'max_length': '名称太长了'
    })
    email = forms.EmailField(label='邮箱', error_messages={
        'required': '请填写邮箱',
        'invalid': '无效的邮箱'
    })
    content = forms.CharField(label='内容', error_messages={
        'required': '请填写内容',
    })


class UserForm(forms.Form):
    username = forms.CharField(label='用户', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
