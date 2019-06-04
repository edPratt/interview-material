"""
Problem description:
    Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

import random

class _Solution:
    def f(self, input):
        random_element = None
        for i, e in enumerate(input):
            print("item: ", e)
            probability = random.randint(1, i+1)
            print(probability, random_element)
            if i == 0:
                random_element = e
            elif probability == 1:
                random_element = e
            print(probability, random_element)
        return random_element


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

    run_print(s.f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

