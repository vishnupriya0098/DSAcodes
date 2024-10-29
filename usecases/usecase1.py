class Solution:
    def twoSum(self,nums,target):
        indices={}
        for i,num in enumerate(nums):
            result=target-num
            if result in indices:
                return [indices[result],i]
            indices[num]=i
Sol=Solution()
print(Sol.twoSum([2,7,11,15],9))
        