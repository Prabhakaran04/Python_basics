import re
# str1 = 'Hello World'
# pattern = r'World'
# result = re.sub(pattern, 'Prabhakaran', str1)
# print(result)


str1 = "The Supermarine S.4 was a 1920s British single-engined monoplane built by Supermarine to race in the 1925 Schneider Trophy contest. To reduce drag forces and thereby increase speed, the company's chief designer, R. J. Mitchell, produced a floatplane of revolutionary design. Built of wood, and with an unbraced cantilever wing, it was powered by a Napier Lion engine developed to produce 700 horsepower (520 kW) over a short racing period. Less than a month after its maiden flight on 24 August 1925, it raised the world's seaplane speed record to 226.752 miles per hour (364.922 km/h). On 23 October, during navigation trials prior to the contest, the aircraft was performing well when, for reasons that have not been fully explained, it went out of control and was destroyed when it dived into the sea from 100 feet (30 m), injuring the pilot."
pattern = r'the'
pattern1 = r'was'
result = re.findall(pattern, str1)
result1 = re.findall(pattern1, str1)
print("The total count of 'the' is: ", len(result))
print("The total count of 'was' is: ", len(result1))

# str1 = 'PrabhaKaran'
# pattern = r'[a-z]'
# result = re.findall(pattern, str1)
# print(result)

# import re

# line = "Cats are smarter than dogs"
# pattern = r'(.*) are (.*?) .*'
# searchObj = re.search(pattern, line, re.M | re.I)
# print(searchObj.group())
# print(searchObj.group(1))
# print(searchObj.group(2))

# str1 = 'East West North South'
# pattern = r'South'
# result = re.search(pattern, str1)
# print(result)


# str1 = 'Prabhakaran'
# pattern = r'a[a-z]'
# result = re.sub(pattern, '$', str1)
# print(result)
