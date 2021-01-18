import re
def kek(nat):
    print(nat.group(0)[1].upper())
    return nat.group(0)[1].upper()
def to_camel_case(text):
    #text="-"+text
    text = re.sub(r'-[a-z]|_[a-z]', kek, text, flags=re.IGNORECASE)
    return text
