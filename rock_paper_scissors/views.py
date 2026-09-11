import random
from django.http import HttpResponse


def game(request):
    choices = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(choices)

    return HttpResponse(
        f"""
        <h1>Rock Paper Scissors</h1>

        <p>Computer chose: {computer_choice}</p>

        <p>Choose one:</p>
        <p>Rock | Paper | Scissors</p>
        """
    )