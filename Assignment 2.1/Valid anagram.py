# Valid anagram

def validAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    f1={}
    f2={}
    for i in s1:
        if i in f1:
            f1[i]+=1
        else:
            f1[i]=1

    for j in s2:
        if j in f2:
            f2[j]+=1
        else:
            f2[j]=1

    for key in f1:
        if key not in f2 or f1[key]!=f2[key]:
            return False

    return True 

#Alternate solution
# from collections import Counter
# def validAnagram(s1,s2):
#     if len(s1)!=len(s2):
#         return False
    
#     Counter(s1)==Counter(s2):
        
