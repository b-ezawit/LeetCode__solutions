class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        #skill = [3,2,5,1,3,4]
        #[1,2,3,3,4,5]
        skill.sort()
        l,r = 0,len(skill)-1
        pairs = []
        while l<r:
            pairs.append((skill[l],skill[r]))
            l += 1
            r -= 1

        pair_sum = pairs[0][0] + pairs[0][1]
        for i in range(1,len(pairs)):
            curr_sum = pairs[i][0] + pairs[i][1]
            if pair_sum != curr_sum:
                return -1
        
        chemistry = 0
        for p1,p2 in pairs:
            chemistry += p1 * p2
        return chemistry
        