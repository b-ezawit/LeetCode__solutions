class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        def recursion_solution(n):
            if n in visit:
                return False
            if n == 1:
                return True
            visit.add(n)
            n_str = str(n)
            sum_digits = 0
            for c in n_str:
                sum_digits += int(c) ** 2

            n = sum_digits
            
            return recursion_solution(n)
        
        return recursion_solution(n)