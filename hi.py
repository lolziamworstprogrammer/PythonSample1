import random
points = 0
questions = 10

a = random.randint(1, 12)
b = random.randint(1, 12)
ans = a + b
running = True

while running:
    innput = int(input(f"what is {a} + {b}?"))
    if ans == innput:
        print("Correct")
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        ans = a + b
        points += 1
        questions -= 1
    else:
        print("wrong")
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        ans = a + b
        questions -= 1
        points -= 1
    if questions == 0:
        print(f"your score is {points}/10")
        running = False