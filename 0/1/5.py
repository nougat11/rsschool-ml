import collections
def duplicate_count(text):
    c = collections.Counter()
    text = text.lower()
    for i in text:
        c[i] += 1
    ans = 0
    for key in c:
        if c[key]>1:
            ans+=1
    return ans
        
    
