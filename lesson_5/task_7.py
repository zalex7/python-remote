import json

with open("text_7.txt", "r", encoding="utf-8") as f:
    base_list = [line.strip("\n").split() for line in f.readlines()]
base_dict = {el[0]: int(el[2]) - int(el[3]) for el in base_list}
profit = [value for value in base_dict.values() if value > 0]
avr_profit = sum(profit) / len(profit)
main_list = [base_dict, {"average_profit": avr_profit}]
print(main_list)

with open("text_7_new.json", "w", encoding="utf-8") as wf:
    json.dump(main_list, wf, ensure_ascii=False, indent=4, sort_keys=True)
