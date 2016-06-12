import sys
import recursive_definitions

out = open(sys.argv[1] + "_solution", 'w')

N = 0
baseCases = set()
recursiveDefs = set()

with open(sys.argv[1], 'r') as file:
    N = int(file.readline())
    for s in file.readline().split():
        baseCases.add('' if s.lower() == 'empty' else s)
    for s in file.readline().split():
        recursiveDefs.add(s)

def writeSolution(n, solutionSet):
    line = 'At step: {}, the possible words are: {}\n'.format(n, solutionSet)
    out.write(line)

recursive_definitions.getStringsUntilNRecursiveStep(baseCases, recursiveDefs, N, callback=writeSolution)

out.close()
