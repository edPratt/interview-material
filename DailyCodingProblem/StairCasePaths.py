"""
recurrence algorithm: ways(n) = ways(n-1) + ways(n-2)

"""

class RecursiveSolution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

    def num_unique_staircase_paths(self, n):
        return self.fib(n + 1)
class DynamicProgrammingSolution:
    def fibonacci(self, n):
        FibArray = [0, 1]

        while len(FibArray) < n + 1:
            FibArray.append(0)

        if n <= 1:
            return n
        else:
            if FibArray[n - 1] == 0:
                FibArray[n - 1] = self.fibonacci(n - 1)
            if FibArray[n - 2] == 0:
                FibArray[n - 2] = self.fibonacci(n - 2)

        FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
        return FibArray[n]

    def num_unique_staircase_paths(self, n):
        return self.fibonacci(n + 1)




def run_print(fn, value):
    print("{0}({1})".format(fn.__name__, value), fn(value))

if __name__ =="__main__":
    from timeit import default_timer as timer

    s = RecursiveSolution()
    #s = DynamicProgrammingSolution()

    run_print(s.num_unique_staircase_paths, 1)
    run_print(s.num_unique_staircase_paths, 2)
    run_print(s.num_unique_staircase_paths, 3)
    run_print(s.num_unique_staircase_paths, 10)
    start = timer()
    run_print(s.num_unique_staircase_paths, 30)
    end = timer()
    print(end - start)
