import re
def solution(s):
    k=[]
    if (len(s)% 2 ==1):
        k = [s[-1] + '_']
    s = [s[i] + s[i+1] for i in range(0, len(s) - len(s) % 2, 2)]
    s+=k
    return s
    
