class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num_to_char = {i: chr(ord('a') + i - 1) for i in range(1, 27)}
        string = ['a'] * n
        remaining = k - n
        ind = n - 1
        
        while remaining > 0:
            add = min(25, remaining)  # 'a' + 25 = 'z'
            string[ind] = num_to_char[1 + add]
            remaining -= add
            ind -= 1
        
        return ''.join(string)
