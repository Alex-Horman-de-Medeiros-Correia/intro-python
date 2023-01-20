import re

pattern = '[A-Z]+[a-z]+$'
x = re.search(pattern, 'aaaaAa')

print(x.span()[0])
