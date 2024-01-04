from django import forms
from . import models


class CreateQuizFromFileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ['text']


# class StartQuizForm(forms.ModelForm):
#     class Meta:
#         model = models.Quiz
#         fields = ['title']
#
#
# class StartQuestionForm(forms.ModelForm):
#     class Meta:
#         model = models.Question
#         fields = ['title']

class StartChoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-check-input position-absolute top-50 end-0 me-3 fs-5"

    class Meta:
        model = models.Choices
        fields = ['select', 'title']

