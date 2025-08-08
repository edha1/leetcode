class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        ns1 = sorted(s1) # sorts strings
        ns2 = sorted(s2) 

        if all(ns1[i] >= ns2[i] for i in range(len(ns1))):
            return True

        if all(ns2[i] >= ns1[i] for i in range(len(ns1))):
            return True

        return False

        