def unique_elements(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            for sub_item in unique_elements(item):
                if sub_item not in result:
                    result.append(sub_item)
        else:
            if item not in result:
                result.append(item)
    return result
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))