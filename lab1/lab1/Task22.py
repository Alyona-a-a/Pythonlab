def type_check(*types):
    def dec(func):
        def wrapper(*args):
            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError("error type")
            result = func(*args)
            return result
        return wrapper
    return dec

@type_check(int, int)
def add(a, b):
    print(a + b)
    add(2, 3)