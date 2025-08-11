class Solution(object):
    def maxEnergyBoost(self, A, B):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        """
        a = b = 0
        for i in range(len(A)):
            a, b = max(a + A[i], b), max(b + B[i], a)
        return max(a, b)
