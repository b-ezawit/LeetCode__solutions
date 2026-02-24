class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        responses = list(map(set,responses))
        print(responses)
        hmap = {}
        for set_s in responses:
            for s in set_s:
                hmap[s] = hmap.get(s,0) + 1
        max_freq = max(hmap.values())
        res = [key for key,val in hmap.items() if val==max_freq]
        res.sort()
        return res[0]