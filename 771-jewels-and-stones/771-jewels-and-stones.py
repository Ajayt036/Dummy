class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        e = []
        for i in stones:
            if i in jewels:
                e.append(i)
        return len(e)