#!/usr/bin/env python3

import sys

ana = {}

with open(sys.argv[1]) as fin:
    for line in fin:
        ls = line.strip().split('\t')
        if not ls:
            continue
        ana[ls[0]] = ls[1:]

wc = 0
ac = 0
        
with open(sys.argv[2]) as fin:
    for line in fin:
        for word in line.split():
            wc += 1
            al = ana.get(word, ['*'+word])
            ac += len(al)
            a = '/'.join(al)
            print(f'^{word}/{a}$', end=' ')
        print('^./.<sent>$')
print(f'words: {wc}, analyses: {ac}, ambiguity: {round(100.0*ac/wc-100,2)}%', file=sys.stderr)
