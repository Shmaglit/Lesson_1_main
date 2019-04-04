# 1. Даны два произвольных списка. Удалите из первого списка элементы, присутствующие во втором.
#
#    Примечание. Списки создайте вручную, например:
#
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
print(my_list_1)
print(my_list_2)
result = []

for list in my_list_1:
    if list not in my_list_2:
        result.append(list)

my_list_1 = result


print('результат:', my_list_1)


