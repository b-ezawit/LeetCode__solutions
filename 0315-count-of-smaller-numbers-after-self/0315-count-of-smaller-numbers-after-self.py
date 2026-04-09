class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0]*len(nums)
        arr = [[nums[i],i] for i in  range(len(nums))]
        def merge_sort(arr):
            if len(arr) <=1:
                return arr
            
            mid = len(arr)//2
            left_part = merge_sort(arr[:mid])
            right_part = merge_sort(arr[mid:])

            return merge(left_part,right_part)
        

        def merge(left,right):
            i=j=0
            merged = []
            while i<len(left) and j<len(right):
                if left[i][0] > right[j][0]:
                    merged.append(right[j])
                    j += 1
                else:
                    val,indx = left[i]
                    counts[indx] += j
                    merged.append(left[i])
                    i += 1
            while i<len(left):
                val,indx = left[i]
                counts[indx] += j
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(arr)
        return counts
