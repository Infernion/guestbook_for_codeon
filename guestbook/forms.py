from django import forms
from guestbook.models import GuestBookModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class GuestBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GuestBookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = GuestBookModel
        fields = ('user_name', 'content')

