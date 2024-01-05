
from django.core.exceptions import ValidationError
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

class AnswerForm(forms.Form):
    question = forms.IntegerField()
    choice = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        question_id = cleaned_data.get("question")
        choice_id = cleaned_data.get("choice")

        valid_query = models.Choices.objects.filter(
            question_id=question_id, id=choice_id
        )

        if not valid_query.exists():
            raise ValidationError(
                f"invalid choice `{choice_id}` for question `{question_id}`"
            )


# class StartChoiceForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs[
#                 "class"
#             ] = "form-check-input position-absolute top-50 end-0 me-3 fs-5"

#     class Meta:
#         model = models.Choices
#         fields = ["select", "title"]

