class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        def recursion_solution(num):
            if num in visit:
                return False
            if num == 1:
                return True
            visit.add(num)
            num_str = str(num)

            sum_digits = 0
            for char in num_str:
                sum_digits += int(char) ** 2

            num = sum_digits
            
            return recursion_solution(num)
        
        return recursion_solution(n)