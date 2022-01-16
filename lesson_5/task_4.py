ru_numbers = {
    "1": "Один",
    "2": "Два",
    "3": "Три",
    "4": "Четыре",
    "5": "Пять",
    "6": "Шесть",
    "7": "Семь",
    "8": "Восемь",
    "9": "Девять",
    "10": "Десять"
}
with open("text_4.txt", "r", encoding="utf-8") as f:
    with open("text_4_new.txt", "w", encoding="utf-8") as fn:
        for line in f:
            line_list = line.split()
            fn.write(f"{ru_numbers[line_list[2]]} {line_list[1]} {line_list[2]} \n")

#  ------------------------------------------- вариант решения ---------------------------------------------------------
import googletrans

translator = googletrans.Translator()
with open("text_4.txt", "r", encoding="utf-8") as f:
    with open("text_4_new.txt", "w", encoding="utf-8") as fn:
        for line in f:
            line_list = line.split()
            fn.write(f"{translator.translate(line_list[0], dest='ru').text} {line_list[1]} {line_list[2]} \n")
