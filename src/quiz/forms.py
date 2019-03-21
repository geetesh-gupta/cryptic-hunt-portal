from django import forms
from quiz.models import Quiz


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your answer here',
                'class': 'col-8 col-md-4 mx-auto'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)  # populates the post
        # instance = kwargs.pop('instance')
        # self.fields['question'] = forms.CharField(label='question')
        # self.fields['question'].queryset = instance.questions.all().filter(order=instance.current_question).all()[0]

    class Meta:
        model = Quiz
        fields = []

    def save(self, commit=True):
        return super(AnswerForm, self).save(commit=commit)
