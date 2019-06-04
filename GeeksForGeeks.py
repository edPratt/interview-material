class BinaryNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key


class LCS():
  def naive_recursion_lcs(X, Y, m, n): 
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 

# Tabulation is bottom up memoization since the original problem is at the bottom of the computation
# Difference is in how you fill the entries of the cache
def tabulated_lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in xrange(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])
            import pprint
            print(X, Y)
            print(X[i-1], Y[j-1])
            print(i, j)
            pprint.pprint(L)
            print('')
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
#end of function lcs

# Memoization is top down
def memoized_lcs(X, Y):
  pass

X = "AGGTAB"
Y = "GXTXAYB"
# result = tabulated_lcs(X, Y)
# print "Length of LCS is ", result





# A Python Program to check if the given 
# string is a pangram or not 
  
def checkPangram(s): 
    List = [] 
    # create list of 26 charecters and set false each entry 
    for i in range(26): 
        List.append(False) 
          
    #converting the sentence to lowercase and iterating 
    # over the sentence  
    for c in s.lower():  
        if not c == " ": 
            # make the corresponding entry True 
            List[ord(c) - ord('a')]=True 
              
    #check if any charecter is missing then return False 
    for ch in List: 
        if ch == False: 
            return False
    return True
  
# Driver Program to test above functions 
sentence = "The quick brown fox jumps over the little lazy dog"
  
if (checkPangram(sentence)): 
    print '"'+sentence+'"'
    print "is a pangram"
else: 
    print '"'+sentence+'"'
    print "is not a pangram"