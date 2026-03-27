class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        checked = {}
        res = 0

        for ans in answers:
            if ans == 0:
                res += 1
            elif (ans not in checked) or( ans in checked and checked[ans] >= ans + 1):
                res += ans + 1

            checked[ans] = checked.get(ans,0) + 1

            if checked[ans] >= ans + 1:
                del checked[ans]
        return res



        