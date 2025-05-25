class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        typed_length = len(word1)
        source_length = len(word2)

        minimum_matrix = [[0 for _ in range(source_length + 1)] for _ in range(typed_length + 1)]

        for i in range(1, source_length + 1):
            minimum_matrix[0][i] = i
        for j in range(1, typed_length + 1):
            minimum_matrix[j][0] = j

        for sour in range(0, source_length):
            for typet in range(0, typed_length):
                if word2[sour] == word1[typet]:
                    minimum_matrix[typet + 1][sour + 1] = minimum_matrix[typet][sour]
                else:
                    minimum_matrix[typet + 1][sour + 1] = min(minimum_matrix[typet][sour],
                                                              minimum_matrix[typet + 1][sour],
                                                              minimum_matrix[typet][sour + 1]) + 1
        return minimum_matrix[typed_length][source_length]
