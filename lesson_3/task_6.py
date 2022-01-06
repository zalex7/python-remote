def int_func(word):
    allowed_symbols = 'abcdefghijklmnopqrstuvwxyz'
    for letter in word:
        if letter not in allowed_symbols:
            return ""
    if word.islower():
        return word.title()
    else:
        return ""


s = "nice авп ъghj jапро hjjпаро Fапрghgh cool"
s_out = ''
for el in s.split():
    result = int_func(el)
    if result != "":
        s_out += result + " "
print(s_out)
