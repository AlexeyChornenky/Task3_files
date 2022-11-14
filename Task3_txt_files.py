files = ('1.txt', '2.txt', '3.txt')
sum_list = []
for file in files:
    with open(file, 'r', encoding='UTF-8') as txt_file:
        file_list = txt_file.readlines()
        inter_list = [file, '\n', str(len(file_list)), '\n', file_list, '\n']
        sum_list.append(inter_list)


def sort_len(some_list):    # функция для сортировки по второму аргументу списка
    return some_list[1]


sum_list.sort(key=sort_len)  # сортировка по второму аргументу списка


with open('summary.txt', 'w', encoding='UTF-8') as summary:
    for object in sum_list:  # распаковка списка и запись
        for element in object:
            summary.writelines(element)