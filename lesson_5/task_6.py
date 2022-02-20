base_dict = {}
with open("text_6.txt", "r", encoding="utf-8") as f:
    for line in f:
        line_list = [el for el in line.split() if el != "-"]
        base_dict[line_list[0][:-2]] = sum(map(int, [el[:el.find("(")] for el in line_list[1:]]))
    print(base_dict)
