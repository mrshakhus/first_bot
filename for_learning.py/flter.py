# def custom_filter(some_list):
#     new_list = [num for num in some_list if type(num) == int and num % 7 == 0]
#     if sum(new_list) <= 83:
#         return True
#     return False

# some_list = [7, 14, 28, 32, 32]

# print(custom_filter(some_list))

# anonymous_filter = lambda str: len([lett for lett in str if lett.lower() == 'я']) >= 23
# print(anonymous_filter('Я - последняя буква в алфавите!'))
# print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))

import sys

print(sys.path)