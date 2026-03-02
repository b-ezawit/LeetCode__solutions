class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = y_x = 0
        min_swaps = 0
        for char1,char2 in zip(s1,s2):
            if char1 != char2:
                if char1 == 'x':
                    x_y += 1
                else:
                    y_x += 1
        if (x_y + y_x) % 2 == 1:
            return -1

        min_swaps += x_y // 2
        min_swaps += y_x // 2

        if x_y % 2 == 1:
            min_swaps += 2
            #if the total count sum of x_y and y_x is even and x_y is odd, it means y_x is odd too and there will be one x_y left from the total x_y's and one y_x left, forming a pair of x_y with y_x --which needs two swaps
        
        return min_swaps
            

