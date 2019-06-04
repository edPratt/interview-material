"""
#2
Uber
Given an array of integers, return a new array such that each element at index i of the new array is the product of 
    all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

##########    Approach #1    #############
def product_of_array(numberArray):
    # TODO: use lambda
    result = 1
    for num in numberArray:
        result *= num
    return result

def product_array_puzzle(numberArray):
    result = []
    for index, num in enumerate(numberArray):
        product = product_of_array(numberArray[:index] + numberArray[index+1:])
        result.append(product)
    return result

# print('product_of_array([1, 2, 3]) == 6', product_of_array([1, 2, 3]))
# print('product_of_array([1, 2, 3]) == 120', product_of_array([1, 2, 3, 4, 5]))

# print('product_array_puzzle([]) == []', product_array_puzzle([]))
# print('product_array_puzzle([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]', product_array_puzzle([1, 2, 3, 4, 5]))


##########    Approach #2    #############
def product_of_array_using_division(numberArray):
    product_all_nums = 1
    for num in numberArray:
        product_all_nums *= num
    
    return [product_all_nums//x for x in numberArray]

print('product_of_array_using_division([]) == []', product_of_array_using_division([]))
print('product_of_array_using_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]', product_of_array_using_division([1, 2, 3, 4, 5]))
