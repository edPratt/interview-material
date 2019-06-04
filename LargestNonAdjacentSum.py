def largest_non_adjacent_sum(integer_array):
    incl = 0
    excl = 0

    for i in integer_array:
        new_excl = excl if excl > incl else incl
        incl = excl + i
        excl = new_excl
        print('new_excl:', new_excl, 'incl:', incl, 'excl', excl)
    return (excl if excl > incl else incl)

def print_fun(args, fn):
    print(args, fn(args))

if __name__ == "__main__":
    print_fun([2, 4, 6, 2, 5], largest_non_adjacent_sum)