import re
def disemvowel(string):
    string = re.sub(r'[aeiou]', '', string, flags=re.IGNORECASE)
    return string
