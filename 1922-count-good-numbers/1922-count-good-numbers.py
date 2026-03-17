class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def pow(x,e):
            if e == 0:
                return 1
            half = pow(x,e//2)
            if e%2 == 0:
                return (half * half) % mod
            else:
                return (half*half*x) % mod
        
        even_count = (n+1) // 2
        odd_count = n//2
        return (pow(5,even_count)*pow(4,odd_count)) % mod
        
            



