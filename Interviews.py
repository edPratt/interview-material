import unittest


class InterviewQuestions():

  @staticmethod
  def MergeTwoSortedLists(a, b):
    result = []
    pointerA, pointerB = 0, 0
    while (pointerA < len(a) and pointerB < len(b)):
      intA, intB = a[pointerA], b[pointerB]
      if (intA < intB):
        result.append(intA)
        pointerA+=1
      else:
        result.append(intB)
        pointerB+=1
      print(intA, intB, result)
    if (pointerA < len(a)):
      result.extend(a[pointerA:])
    if (pointerB < len(b)):
      result.extend(b[pointerB:])
    return result



class Test(unittest.TestCase):
  def TestMergeTwoSortedLists(self):
    self.assertEqual(InterviewQuestions.MergeTwoSortedLists([1, 3, 5, 7], 
                                                            [2, 4, 6, 8, 9]), 
                                                            [1, 2, 3, 4, 5, 6, 7, 8, 9])
    large1, large2 = [], []
    for i in xrange(100000):
      # odd number
      if (i % 2):
        large2.append(i)
      # even number
      else:
        large1.append(i)
    large3 = InterviewQuestions.MergeTwoSortedLists(large1, large2)

if __name__ == "__main__":
  unittest.main()    