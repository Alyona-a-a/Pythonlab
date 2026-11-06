def flatten_list(lst):
    index = 0
    while index < len(lst):
        if isinstance(lst[index], list):
            nested = lst.pop(index)
            for item in reversed(nested):
                lst.insert(index, item)
            flatten_list(lst)
        else:
            index += 1
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)