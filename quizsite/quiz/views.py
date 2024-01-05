from django.shortcuts import render, redirect
from . import forms, models
from django.views import View
from django.views.generic import ListView
from django.http import Http404, JsonResponse
from django.forms import formset_factory
from collections import Counter


# Create your views here.

class CreateQuizForm(View):
    def get(self, request):
        form = forms.CreateQuizFromFileForm()
        return render(request=request, template_name='quizmaker.html', context={'form': form})

    def post(self, request):
        form = forms.CreateQuizFromFileForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('text').splitlines()
            quiz_name = models.Quiz(title=content[0], slug=content[0].replace(" ", "-"))
            quiz_name.save()
            count_nls = 0
            res_list = []
            for i in range(len(content)):
                if count_nls == 2:
                    count_nls = 0
                    continue
                count_nls = 0
                j = i
                while content[j] == "":
                    j += 1
                    count_nls += 1
                if count_nls == 1:
                    res = models.Result(title=content[i + 1], description=content[i + 2], quiz=quiz_name)
                    res_list.append(res)
                    res.save()
                elif count_nls == 2:
                    question = models.Question(title=content[i + 2], quiz=quiz_name)
                    question.save()
                    k = i + 3
                    choice_counter = 0
                    while content[k] != "":
                        if choice_counter > len(res_list) - 1 or content[k] == 'end':
                            break
                        choice = models.Choices(quiz=quiz_name, title=content[k], question=question,
                                                result=res_list[choice_counter])
                        choice.save()
                        choice_counter += 1
                        k += 1
            return render(request=request, template_name='successful.html')
        return redirect('quiz')


class QuizView(ListView):
    model = models.Quiz
    template_name = 'index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(published=True)


# class StartView(View):
#
#     # def get(self, request, slug=None):
#     #     choices = []
#     #     qc = {}
#     #     forms_list = []
#     #     quiz_object = None
#     #     if slug is not None:
#     #         try:
#     #             quiz_object = models.Quiz.objects.get(slug=slug)
#     #             questions = quiz_object.question_set.all()
#     #             for item_1 in questions:
#     #                 qc[item_1.title] = []
#     #                 for item_2 in item_1.choices_set.all():
#     #                     qc[item_1.title].append(forms.StartChoiceForm(instance=item_2, auto_id='listGroupRadioGrid1%s',
#     #                                                                   initial={'select': False, }))
#     #             context = {'qc': qc, }
#     #
#     #         except models.Quiz.DoesNotExist:
#     #             raise Http404
#     #         return render(request=request, template_name='quiz-main.html', context=context)
#     #
#     # def post(self, request, slug):
#     #     quiz_object = models.Quiz.objects.get(slug=slug)
#     #     questions = quiz_object.question_set.all()
#     #     choices = quiz_object.choices_set.all()
#     #     for _ in choices:
#     #         form = forms.StartChoiceForm(request.POST)
#     #         if form.is_valid():
#     #             print(form.cleaned_data)
#     #             return render(request, template_name="result.html")

class StartView(View):
    form_model = forms.AnswerForm

    def get_quiz_or_404(self, slug):
        queryset = models.Quiz.objects.filter(slug=slug).prefetch_related(
            "question_set", "question_set__choices_set"
        )
        try:
            return queryset.get()
        except models.Quiz.DoesNotExist:
            raise Http404(f"quiz with slug `{slug}` not found")

    def get(self, request, slug=None):
        quiz = self.get_quiz_or_404(slug)
        return render(
            request=request,
            template_name="quiz-main.html",
            context={
                "questions": quiz.question_set.all(),
                "formset": formset_factory(
                    self.form_model,
                    extra=quiz.question_set.count(),
                ),
            },
        )

    def post(self, request, slug):
        quiz = self.get_quiz_or_404(slug)
        FormSet = formset_factory(self.form_model)
        data = request.POST.copy()
        data.update({'form-TOTAL_FORMS': quiz.question_set.count()})
        formset = FormSet(data)
        if not formset.is_valid():
            return render(
                request=request,
                template_name="quiz-main.html",
                context={
                    "questions": quiz.question_set.all(),
                    "formset": formset_factory(
                        self.form_model,
                        max_num=quiz.question_set.count(),
                    ),
                    "errors": formset.errors,
                },
            )
        results_list = []
        results_dict = {}
        maximum = 0
        res = None
        choices = quiz.choices_set.all()
        results = quiz.result_set.all()
        for answer in formset.cleaned_data:
            for choice in choices:
                if choice.id == answer['choice']:
                    results_list.append(choice.result)
        for k, v in Counter(results_list).items():
            results_dict[k] = v
        for key, value in results_dict.items():
            if value > maximum:
                maximum = value
                res = key

        return render(request=request, template_name="result.html", context={'res': res})  # Should be a redirect
