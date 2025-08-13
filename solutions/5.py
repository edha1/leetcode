class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lP = 0 
        maxS = ""

        if not s:
            return ""
        for i in range(len(s)): 

            # odd length palindrome 
            l = i - 1
            r = i + 1 
            count = 1
            while l >= 0 and r < len(s): 
                if s[l] != s[r]: 
                    break 
                count += 2
                l -= 1 
                r += 1 
            if count > lP: 
                lP = count 
                maxS = s[l+1:r]

            # even length palindrome
            l = i
            r = i + 1 
            count = 0
            while l >= 0 and r < len(s): 
                if s[l] != s[r]: 
                    break 
                count += 2
                l -= 1 
                r += 1 
            if count > lP: 
                lP = count 
                maxS = s[l+1:r]

 


                
        
        return maxS