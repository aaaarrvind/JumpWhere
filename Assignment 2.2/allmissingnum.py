#LC 488

def allmissingnum(nums):
    n=len(nums)
    set_num=set(nums)
    return [i for i in range(1, n+1) if i not in set_num]