class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start=0
        window_max=sum(nums[:k])
        window_current=window_max
        for i in nums:
            if (k+start)<len(nums):
                window_sum=window_current-i+nums[k+start]
                window_current=window_sum
                if window_sum>window_max:
                    window_max=window_sum
                start+=1
        max_avg=(window_max)/k
        return max_avg
                
                
        
        
        