import sys
import itertools

del sys.argv[0]

with open('dictionary.txt', 'w') as f:
    for item in itertools.permutations(sys.argv):
        f.write("%s\n" % ''.join(item))
