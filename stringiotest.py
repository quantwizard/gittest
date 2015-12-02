#!/usr/bin/env python

"""
Simple examples with StringIO module
"""

# Find the best implementation available on this platform

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

# Writing to a buffer
output = StringIO()
output.write('This goes into the buffer. ')

print >>output, 'And so does this.'
# Retrieve the value written
print output.getvalue()

output.close() # discard buffer memory

# Initialize a read buffer
input = StringIO('Inital value for read buffer')

# Read from the buffer
print input.read()