class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: 
            return False 

        occur = [0] * 128 

        for i in range(len(s)): 
            occur[ord(s[i])] += 1

        i = 0 
        a = 0 
        while occur[i] == 0: 
            i += 1 
        
        a = occur[i]

        while i < len(occur): 
            if occur[i] != 0 and occur[i] != a: 
                return False 
            i += 1

        return True 

        