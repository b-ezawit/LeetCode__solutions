class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        pop_changes = [0] * 101
        
        for birth, death in logs:
            pop_changes[birth - 1950] += 1 
            pop_changes[death - 1950] -= 1 
            
        max_pop = 0
        earliest_year = 1950
        current_pop = 0
        
        # Step 2: Sweep through the years to find the prefix sum
        # 
        for i in range(101):
            current_pop += pop_changes[i]
            
            # If we find a new maximum, update the year
            # Since we iterate from 1950 upwards, we naturally get the EARLIEST year
            if current_pop > max_pop:
                max_pop = current_pop
                earliest_year = 1950 + i
                
        return earliest_year