#Twosum LC#1
def twoSum(target, nums):
        hashmap={}
        for ind, val in enumerate(nums):
            comp= target-val
            if comp in hashmap:
                return [hashmap[comp] ,ind ]
            hashmap[val]=ind
        
        return[]