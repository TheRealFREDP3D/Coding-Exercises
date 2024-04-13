# Magic 8 Ball
# Answers randomly to any Yes or No questions.

import random

num = random.randint(1, 9)

answers = [
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

input("Question: ")
print(f"Magic 8 Ball: {answers[num]}")
