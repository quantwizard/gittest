import re
tester = "5/results"

reg = re.compile(r'(?P<id>[0-9]+)/results')
print reg.match(tester).group('id')
