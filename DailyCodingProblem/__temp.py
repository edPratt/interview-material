"""
Problem description:
"""

class _Solution:
    def f(self):
        pass

def run_print(fn, value):
    print("{0}({1})".format(fn.__name__, value), fn(value))

def runtime_analysis():
    from timeit import default_timer as timer
    start = timer()
    print('test runtime')
    end = timer()
    print(end - start)

if __name__ == "__main__":
    s = _Solution()

    run_print(s.f, 1)

