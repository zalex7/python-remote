my_int = 1
my_real = 2.5
my_complex = 5 + 8j
my_str = "простая строка"
my_list = [1, 2, 3]
my_tuple = ("q", "w", "e", "r")
my_set = {0, 100, 1000}
my_dict = {1: "a", 2: "b", 3: "c"}
my_bool = True
my_bytes = b'text'
my_bytearray = bytearray(b"some text")
my_None = None
all_in_list = [my_int, my_real, my_complex, my_str, my_list, my_tuple, my_set, my_dict, my_bool, my_bytes, my_bytearray,
               my_None]

for ind, el in enumerate(all_in_list, 1):
    print(ind, el, type(el))
