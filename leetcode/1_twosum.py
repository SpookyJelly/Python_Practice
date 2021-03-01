class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1+i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

'''
결과 :

Success Details 
Runtime: 48 ms, faster than 65.32% of Python3 online submissions for Two Sum.
Memory Usage: 14.6 MB, less than 13.08% of Python3 online submissions for Two Sum.

'''