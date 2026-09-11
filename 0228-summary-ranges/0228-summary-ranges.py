class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        start=nums[0]
        output=[]
        for i in range(len(nums)-1):
            next=nums[i]+1
            if nums[i+1]!=next:
                end=nums[i]
                if start==end:
                    output.append(str(start))
                else:
                    output.append((f"{start}->{end}"))
                start=nums[i+1]
                
            else:
                end=nums[i+1]

        end = nums[-1]
        if start == end:
            output.append(str(start))
        else:
            output.append(f"{start}->{end}")
        return output
        