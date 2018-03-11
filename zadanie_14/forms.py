from wtforms_alchemy import ModelForm

from zadanie_14.models import User, Message, Comment

class UserForm(ModelForm):
    class Meta:
        model = User

class MessageForm(ModelForm):
    class Meta:
        model = Message

        include = ['user_id',]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        include = ['user_id', 'message_id']

