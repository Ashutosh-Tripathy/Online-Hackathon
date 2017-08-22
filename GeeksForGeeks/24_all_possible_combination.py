# obj = {  "name": "John", "age": 31, "city": "New York", "interests":["Swimming", "Music"]}

# def print_data(data):
#     if type(data) is str:
#         print_string(data)
#     elif type(data) is list:
#         print_array(data)
#     elif type(data) is dict:
#         print_object(data)

# def print_string(my_string):
#     print("\n".join(my_string.split()))

# def print_array(my_array):
#     for item in my_array:
#         print_data(item)

# def print_object(obj):
#     for key in obj:
#         print_data(obj[key])
# print_object(obj)

string = "abcdefghijklmnopqrst"
l = len(string)
opsize = pow(2, l - 1)
for i in range(opsize):
    for j in range(l):
        print(string[j], end="")
        if i & 1 << j:
            print(" ", end="")
    print()


# stack = [items[0], items[0] + " "]

# for i in range(1, len(items)):
#     new_stack = []
#     for item in stack:
#         new_stack.append(item + items[i])
#         if i < len(items) - 1:
#             new_stack.append(item + items[i] + " ")
#     stack = new_stack

# for item in stack:
#     print(item)
