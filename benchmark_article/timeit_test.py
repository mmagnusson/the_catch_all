def my_test():
    try:
        8.4567 / 0
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    import timeit
    setup = "from __main__ import my_test"
    print(timeit.timeit("my_test()", setup=setup))


