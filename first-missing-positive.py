"""
#4
Stripe
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

def findPositiveSubArr(arr):
    negativeIndex = 0
    for  i in range(len(arr)):
        if arr[i] <= 0:
            arr.insert(negativeIndex, arr.pop(i))
            negativeIndex += 1

    # print('INSIDE findPositiveSubArr', arr, arr[negativeIndex:])
    return arr[negativeIndex:]

# Returns the first missing positive number
def findMissingPositive(positiveArr):
    l = len(positiveArr)
    for num in positiveArr:
        index = abs(num)-1
        print('num: ', num, 'index: ', index, 'positiveArr: ',positiveArr)
        if index < l and positiveArr[index] > 0:
            positiveArr[index] *= -1
    # print(positiveArr)
    for i in range(l):
        if positiveArr[i] > 0:
            return i+1

    return l+1

if __name__ == "__main__":
    # result = findMissingPositive(findPositiveSubArr([2, 3, -4, 5, -6, 7, 8, 1000, 60]))
    # result = findMissingPositive(findPositiveSubArr([1, 2, 3, -4, 4, 5, 6, -6, 7, 8, 1000, 60]))
    result = findMissingPositive(findPositiveSubArr([20, 21, 22, 23]))
    print(result)