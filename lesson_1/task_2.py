time = int(input("Введите время в секундах:"))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - hours * 3600 - minutes * 60
print(f"Введено следующее время: {'{:02}'.format(hours)}:{'{:02}'.format(minutes)}:{'{:02}'.format(seconds)}")
