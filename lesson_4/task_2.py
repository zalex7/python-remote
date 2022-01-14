source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([source_list[i] for i in range(1, len(source_list)) if source_list[i] > source_list[i - 1]])
