class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        p1 = 0 
        p2 = 0 

        while p2 < len(t) and p1 < len(s): 
            currs = s[p1]
            currt = t[p2]

            if currs == currt: 
                p1 += 1 
                p2 += 1
            else: 
                p2 += 1 

        if p1 < len(s): 
            return False 

        return True 


        