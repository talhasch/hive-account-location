import operator
import csv

from geo import country_code_from_input
from cache import cache_get, cache_set, cache_size, skip_list_get, skip_list_add
from helper import sanitize, should_ignore

import pycountry
import flag

with open('input.csv', 'r') as file:
    data = [sanitize(x) for x in file.readlines() if not should_ignore(x)]

print("Input size: {}".format(len(data)))

group = {}
total = 0

for inpt in data:

    if skip_list_get(inpt) is not None:
        continue
    
    code = cache_get(inpt)

    if code is None:
        code = country_code_from_input(inpt)

        if code is None:
            skip_list_add(inpt)
            continue

        cache_set(inpt, code)

    total += 1

    if code in group:
        group[code] += 1
    else:
        group[code] = 1

sorted_group = sorted(group.items(), key=operator.itemgetter(1), reverse=True)

print('Total detected: {}'.format(total))

print("""
| Country     | Count    |  Percent |
| -------- | -------- | -------- |""")
for i in sorted_group[0:40]:
    [code, count] = i
    name = pycountry.countries.get(alpha_2=code.upper()).name
    em = flag.flag(code.upper())
    perc = 100 * count/total
    print('| {} {} | {} | {}% |'.format(em, name, count, '{:.2f}'.format(perc)))
    