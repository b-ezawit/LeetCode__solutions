class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def comparator(n1,n2):
            if int(n1+n2) > int(n2+n1):
                return -1
            else:
                return 1
        
        s_list = list(map(str,nums))
        ans = sorted(s_list, key=cmp_to_key(comparator))
        return str(int("".join(ans)))

        