from collections import defaultdict

members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]
result = defaultdict(list)
for sex, name in members:
    # result[sex].append(name)
    result[sex].insert(0, name)
print result
