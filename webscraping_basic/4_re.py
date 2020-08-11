# Python Web Scraping

# Title : Regular Expression
# Date : 2020-08-11
# Creator : tunealog

import re

# . (ca.e): Matches any single characterr
#           > care, cafe, case
# ^ (^de) : Matches the starting position within the string
#           > desk, deck
# $ (se$) : Matches the ending position of the string
#           > case, base


def print_match(m):
    if m:
        # Matched String
        print("m.group() :", m.group())
        # Input String
        print("m.string : ", m.string)
        # Start Index
        print("m.start() : ", m.start())
        # End Index
        print("m.end() : ", m.end())
        # Start and End Index
        print("m.span() : ", m.span())
    else:
        print("Not Matched")


# 1. compile
# ca?e
p = re.compile("ca.e")

# 2. match
# Not Matched
m = p.match("good care cafe")
print_match(m)

# 3. search
# m.group() : care
# m.string :  good care cafe
# m.start() :  5
# m.end() :  9
# m.span() :  (5, 9)
m = p.search("good care cafe")
print_match(m)

# 4. findall
# ['care', 'cafe']
lst = p.findall("good care cafe")
print(lst)

####################################
# 1. p = re.compile("")
# 2. m = p.match("")
# 3. m = p.search("")
# 4. lst = p.findall("")
####################################
