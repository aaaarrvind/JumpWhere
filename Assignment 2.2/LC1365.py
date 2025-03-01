from collections import defaultdict 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap={}
        sorted_nums=sorted(nums)
        for i , val in enumerate(sorted_nums):
            if val not in hashmap:
                hashmap[val]=i

        return [hashmap[num] for num in nums]
    
#alternate easy solution Time complexity O(n^2)

def smallerNumbersThanCurrent(nums):
    res=[]
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[j]<nums[i]:
                count+=1 
        res.append(count)

    return res