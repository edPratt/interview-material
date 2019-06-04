import unittest

class StringQuestions():
  class LongestSubstringNoRepeat():
    """
    link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """
    def brute(self, s):
      index = 1
      longest_substring = ""
      for char1 in s:
        temp_substring = char1
        for char2 in s[index:len(s)]:
          if (char2 not in temp_substring):
            temp_substring += char2
          else: 
            break
        if (len(temp_substring) > len(longest_substring)):
          longest_substring = temp_substring
        index += 1
      return len(longest_substring)

    def sliding_window(self, s):
      # # TODO: infinite loop, use pdb
      n = len(s)
      hash_set = set()
      ans, i, j = 0, 0, 0
      while (i < n and j < n):
        print(hash_set)
        print(ans)
        # try to extend the range [i, j)
        if (not hash_set.__contains__(s[j])):
          hash_set.add(s[j])
          j+=1
          ans = max(ans, j - 1)
        else:
          i+=1
          hash_set.remove(s[i])
      return ans

  class NumJewelsInStones():
    def num_jewels_in_stones(self, J, S):
      """
      :type J: str
      :type S: str
      :rtype: int

      Source: https://leetcode.com/problems/jewels-and-stones/submissions/
      
      NOTE: runtime not bad, memory pretty bad
      """
      # O(1) lookup time
      stone_tracker = {}
      
      # Load a dictionary to be used to keep count of letters
      #  once iterating through S
      for character in J:
        stone_tracker[character] = 0
      
      for character in S:
        if (character in stone_tracker.keys()):
          stone_tracker[character] += 1
          
      return sum(stone_tracker.values())


class ArrayQuestions():
  class MaxProfitStockWithCooldown():
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
    """
    def brute(prices_arr):
      
      pass
class Test(unittest.TestCase):

  squestions = StringQuestions()

  global longest_substring

  longest_substring = squestions.LongestSubstringNoRepeat()

  def test_longest_substring_no_repeat_brute_force(self):
    self.assertEqual(longest_substring.brute("abcdf"), 5)
    self.assertEqual(longest_substring.brute("abccdf"), 3)
    self.assertEqual(longest_substring.brute("abbbbcd"), 3)

  def test_longest_substring_no_repeat_sliding_window(self):
    # pass
    # self.assertEqual(longest_substring.longest_substring_no_repeat_sliding_window("abcdf"), 5)
    self.assertEqual(longest_substring.sliding_window("abacdasdghhhhhhhhf"), 5)
    
  
if __name__ == "__main__":
  unittest.main()    
  