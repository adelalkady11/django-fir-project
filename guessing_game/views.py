import random
from django.http import HttpResponse


def game(request):
    number = random.randint(1, 10)

    return HttpResponse(
        f"""
        <h1>Number Guessing Game</h1>

        <p>The secret number is: {number}</p>

        <form>
            <input type="number" placeholder="Guess a number">
            <button type="submit">Guess</button>
        </form>
        """
    )