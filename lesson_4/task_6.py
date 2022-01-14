from itertools import count, cycle

my_list = []
for i in count(3):
    print(i)
    my_list.append(i)
    if i == 10:
        break
print("*" * 20)
cycle_count = 0
for i in cycle(my_list):
    print(i, end=" ")
    cycle_count += 1
    if cycle_count == 100:
        break
