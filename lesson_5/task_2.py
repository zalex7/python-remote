with open("text_2.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    print(f"There are {len(content)} lines in the file.")
    for i, el in enumerate(content, 1):
        print(f"There are {len(el.split())} words in line {i}.")
