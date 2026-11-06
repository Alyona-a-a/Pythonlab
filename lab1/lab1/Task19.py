def cache(func):
    d = {}
    def wrapper(*args):
        if args not in d:
            d[args] = func(*args)
        return d[args]
    return wrapper

@cache
def summaaib(a, b):
    return a + b

print(summaaib(1, 2))
print(summaaib(1, 2))