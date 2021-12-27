str_in = input("Введите строку из нескольких слов разделенных пробелами: ").split()
for word in str_in:
    print(f"{word:.10s}")
