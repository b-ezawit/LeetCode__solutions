class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict2 = {word:i for i,word in enumerate(list2)}
        minSum = float('inf')
        result = defaultdict(int)

        for i,word in enumerate(list1):
            if word in dict2:
                if i + dict2[word] < minSum:
                    minSum = i+dict2[word]
                    result[word] = minSum
                elif i + dict2[word] == minSum:
                    result[word] = minSum
        leastSum = min(result.values())
        return [k for k in result if result[k]==leastSum]





        