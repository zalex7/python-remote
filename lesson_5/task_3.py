with open("text_3.txt", "r", encoding="utf-8") as f:
    base_list = [line.strip("\n").split() for line in f.readlines()]
base = {}
err_count = 0
for i, el in enumerate(base_list, 1):
    if el[0] in base.keys():
        try:
            base[el[0] + "_" + str(i)] = float(el[1])
        except ValueError:
            print(f"Error in element {i}: {el}")
            err_count += 1
            base[el[0] + "_" + str(i)] = 0.0
    else:
        try:
            base[el[0]] = float(el[1])
        except ValueError:
            print(f"Error in element {i}: {el}")
            err_count += 1
            base[el[0]] = 0.0
print(f"{err_count} errors occurred when creating the database.")
print(base)
print("List of employees whose salary is less than 20,000")
print(*[key for key, value in base.items() if value < 20000], sep="\n")
print(f"Average salary of employees is {sum(base.values()) / len(base)}")
