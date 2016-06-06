import sys
from datastructures.set import Set
import relations as rel

set = Set()
N = 0
pairs = []

with open(sys.argv[1], 'r') as file:
    N = int(next(file))
    for line in file:
        pair = line.split()
        set.addAll(pair)
        pairs.append(pair)

properties = []
if rel.isReflexive(pairs): properties.append('REFLEXIVA')
if rel.isIrreflexive(pairs): properties.append('IRREFLEXIVA')
if rel.isTransitive(pairs): properties.append('TRANSITIVA')
if rel.isSymmetric(pairs): properties.append('SIMETRICA')
if rel.isAsymmetric(pairs): properties.append('ASIMETRICA')
if rel.isEquivalent(pairs): properties.append('EQUIVALENTE')

print(properties)
print(set)
