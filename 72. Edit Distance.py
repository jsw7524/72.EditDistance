class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1Length=len(word1)+1
        w2Length=len(word2)+1
        distance=[[0] * w1Length for i in range(w2Length)]

        for i in range(w1Length):
            distance[0][i]=i

        for i in range(w2Length):
            distance[i][0]=i

        for i in range(1,w1Length):
            for j in range(1,w2Length):
                if word1[i-1] == word2[j-1]:
                    distance[j][i]=distance[j-1][i-1]
                else:
                    distance[j][i]=min(distance[j-1][i],distance[j][i-1],distance[j-1][i-1])+1
        return distance[w2Length-1][w1Length-1]

sln=Solution()
assert 3==sln.minDistance("horse","ros")
assert 5==sln.minDistance(word1 = "intention", word2 = "execution")