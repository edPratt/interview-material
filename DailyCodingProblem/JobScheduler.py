import time
def job_scheduler(fn, n):
    """ Calls a function after n milliseconds

    Instructions: Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

    Args:
        fn: any function
        n: a time in milliseconds

    Returns:
        None
    """
    time.sleep(n/1000)
    return fn


if __name__ == "__main__":
    def fn():
        print("fack!")
    job_scheduler(fn, 5000)
    #job_scheduler(print("fack 2!"), 5000)
