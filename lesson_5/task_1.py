with open("text_1.txt", "w", encoding="utf-8") as f:
    while True:
        input_str = input()
        if input_str == "":
            break
        print(input_str, file=f)
