from wtforms_alchemy import ModelForm

from zadanie_13.models import GuestBookItem

class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBookItem