def merge_dicts(dict_a, dict_b):
    for key, value in dict_b.items():
        if key in dict_a:
            if isinstance(dict_a[key], dict) and isinstance(value, dict):
                merge_dicts(dict_a[key], value)
            elif isinstance(dict_a[key], list) and isinstance(value, list):
                dict_a[key].extend(value)
            elif isinstance(dict_a[key], set) and isinstance(value, set):
                dict_a[key].update(value)
            elif isinstance(dict_a[key], tuple) and isinstance(value, tuple):
                dict_a[key] = dict_a[key] + value
            else:
                dict_a[key] = value
        else:
            dict_a[key] = value
dict1 = {"a": {"x": 1}, "b": [1], "c": {1}, "d": (1,), "e": 1}
dict2 = {"a": {"y": 2}, "b": [2], "c": {2}, "d": (2,), "e": 2, "f": 3}

merge_dicts(dict1, dict2)
print(dict1)