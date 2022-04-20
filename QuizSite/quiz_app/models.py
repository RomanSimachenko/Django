from enum import unique
from django.db import models
from django.utils.translation import gettext as _


class Question(models.Model):
    ask = models.CharField("Ask", max_length=1000)
    answer1 = models.CharField("Answer1", max_length=1000)
    answer2 = models.CharField("Answer2", max_length=1000)
    answer3 = models.CharField("Answer3", max_length=1000)
    answer4 = models.CharField("Answer4", max_length=1000)
    right_answer = models.PositiveIntegerField(
        "Right answer", help_text=_("Type number of the right answer"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return f"{self.ask} - {self.right_answer}"


class Answer(models.Model):
    email = models.EmailField("Email", unique=True)
    full_name = models.CharField("Full name", max_length=300, unique=True)
    total = models.PositiveIntegerField("Total")
    correct = models.PositiveIntegerField("Correct")
    wrong = models.PositiveIntegerField("Wrong")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):
        return self.full_name


class Quiz(models.Model):
    name = models.CharField("Name", max_length=200)
    questions = models.ManyToManyField(Question, verbose_name="Questions")
    answers = models.ManyToManyField(
        Answer, verbose_name="Answers", blank=True)

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizs")

    def __str__(self):
        return self.name
