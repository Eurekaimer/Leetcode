class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ranking = []
        ranks = sorted(score, reverse = True)
        ranksIndex = dict()
        for i in range(len(ranks)):
            ranksIndex[ranks[i]] = i
        for s in score:
            rank = ranksIndex[s]
            if rank == 0:
                ranking.append("Gold Medal")
            elif rank == 1:
                ranking.append("Silver Medal")
            elif rank == 2:
                ranking.append("Bronze Medal")
            else:
                ranking.append(str(rank + 1))
        return ranking