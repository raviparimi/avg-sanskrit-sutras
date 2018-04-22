#!/usr/bin/python
import os
# Each element of top-level list points to the adhyaya
sutras = [
# Each element in sub-list points to largest sutra number for that pada
[ 75,  73,  93,  110],
[ 72,  38,  73,  85],
[ 150,  188,  176,  117],
[ 178,  145,  168,  144],
[ 136,  140,  119,  160],
[ 223,  199,  139,  175],
[ 103,  118,  120,  97],
[ 74,  108,  119,  68],
]
if __name__ == '__main__':
    for idx, s in enumerate(sutras):
        adhyaya = idx + 1
        for i, elem in enumerate(s):
            pada = i + 1
            for snum in range(1, elem+1):
                f = '%d-%d-%d' % (adhyaya, pada, snum) + '.html'
                if not os.path.exists(f):
                    print 'MISSING: ', f
