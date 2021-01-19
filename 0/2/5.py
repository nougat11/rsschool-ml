import re
def domain_name(url):
    print(url)
    url = re.split(r'www.|https://|http://|\.',url)
    url = list(filter(None, url))
    print(url)
    return url[0]
