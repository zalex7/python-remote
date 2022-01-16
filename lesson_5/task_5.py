from random import randint

with open("text_5.txt", "w+", encoding="utf-8") as f:
    print(*[randint(0, 100) for _ in range(50)], file=f)
    f.seek(0)
    print(f"The sum of the numbers in the file {f.name} is {sum(map(int, f.read().split()))}.")
