import unittest

class RedditLink1():
  class General():
    def most_frequent_integer_in_array(input_arr):
      """
      TODO: 
        1. Generics
        2. Handle tiebreakers
      """
      integer_dict = {}
      for integer in input_arr:
        if (integer in integer_dict.keys()):
          integer_dict[integer] += 1
        else:
          integer_dict[integer] = 1
      return max(integer_dict, key=integer_dict.get)

class TestGeneral(unittest.TestCase):
  def test_most_frequent_integer_in_array(self):
    arr1 = [1, 6, 3, 8, 8, 3, 5, 7, 8, 3, 8]
    self.assertEqual(RedditLink1.General.most_frequent_integer_in_array(arr1), 8)

if __name__ == "__main__":
  unittest.main()    
