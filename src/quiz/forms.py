from django import forms
from quiz.models import Quiz
from question_answer.models import Question


class AnswerForm(forms.ModelForm):
    question_slug = forms.CharField(widget=forms.HiddenInput())
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
        instance = kwargs.pop('instance')
        questionorder_set = instance.questionorder_set
        question = questionorder_set.filter(quiz=instance, order=instance.current_question)[0].question
        question_slug = question.slug
        self.initial['question_slug'] = question_slug

    class Meta:
        model = Quiz
        fields = []

    def clean_answer(self):
        question_slug = self.cleaned_data['question_slug']
        user_answer = self.cleaned_data['answer']
        pos_answers = Question.objects.all().filter(slug=question_slug)[0].answers.all()
        matches = False
        for pos_answer in pos_answers:
            if (str(user_answer) == str(pos_answer)):
                matches = True
                break

        if not matches:
            raise forms.ValidationError("Wrong Answer!")
        return user_answer

    def save(self, commit=True):
        return super(AnswerForm, self).save(commit=commit)
