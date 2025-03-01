def missingnum(nums):
    arraysum= sum(nums)
    expectedsum= len(nums)*(len(nums)+1)//2
    return expectedsum-arraysum