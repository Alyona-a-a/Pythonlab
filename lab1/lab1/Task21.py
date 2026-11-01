import time

def timing(func):
    def wrapper():
        start = time.perf_counter()
        result = func()
        end = time.perf_counter()
        print(f"{(end - start) * 1000:.3f} мс")
        return result
    return wrapper
@timing
def vyvod():
    chtolibo= input("Введите что-нибудь: ")
    print(f"{chtolibo}")
vyvod()