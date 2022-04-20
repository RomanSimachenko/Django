from django.shortcuts import render
from . import models


def QuizView(request, pk):
    if request.method == "POST":
        post_data = request.POST
        name, email = post_data.get("name"), post_data.get('email')
        quiz = models.Quiz.objects.get(id=pk)
        questions = quiz.questions.all()
        total, correct, wrong = 0, 0, 0
        for question in questions:
            if question.ask in post_data:
                total += 1
                if question.right_answer == int(post_data.get(question.ask)):
                    correct += 1
                else:
                    wrong += 1
        quiz.answers.create(email=email, full_name=name,
                            total=total, correct=correct, wrong=wrong)
        context = {
            "quiz_name": quiz.name,
            "total": total,
            "correct": correct,
            "wrong": wrong,
        }
        return render(request, "quiz_app/result.html", context)
    else:
        quiz = models.Quiz.objects.get(id=pk)
        context = {
            "quiz_name": quiz.name,
            "questions": quiz.questions.all(),
        }
        return render(request, "quiz_app/index.html", context)
