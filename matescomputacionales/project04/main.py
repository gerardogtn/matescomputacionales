import sys
import derivations as d

inputFileName = sys.argv[1]
stringsInFileName = sys.argv[1].split('.')
outputFileName = '_solution.'.join(stringsInFileName)

string = ""
variables = []
terminals = []
startSymbol = 'S'
transformations = {}
derivationType = 'A'
N = 0
M = 0

with open(inputFileName, mode='r') as file:
    string = "".join(file.readline().split())
    variables = file.readline().split()
    terminals = file.readline().split()
    startSymbol = file.readline().split()[0]
    derivationType = file.readline().split()[0]

    if derivationType == 'A':
        N, M = file.readline().split()

    for line in file:
        values = line.split()
        transformations[values[0]] = values[1:]

cfg = (variables, terminals, transformations, startSymbol)
outFile = open(outputFileName, mode='w')

def writeDerivation(derivation):
    markers = []
    strings = []
    for step in derivation:
        for i in range(len(step[0])):
            if i == step[1]:
                markers.append("*")
            else:
                markers.append(" ")
            strings.append(step[0][i])
        markers.append("    ")
        strings.append(" => ")

    outFile.write("{}\n".format("".join(markers)))
    outFile.write("{}\n".format("".join(strings)))

if derivationType == 'A':
    derivations = d.getAllDerivations(cfg, string, MAX_SUBSTITUTIONS=N, MAX_DERIVATIONS=M)
    for der in derivations:
        writeDerivation(der)
        outFile.write("\n{}".format("Next derivation:"))
elif derivationType == 'L':
    derivation = d.getLeftDerivation(cfg, string)
    writeDerivation(derivation)
elif derivationType == 'R':
    derivation = d.getRightDerivation(cfg, string)
    writeDerivation(derivation)
else:
    outFile.close()
    raise RuntimeError("invalid type of derivation; must be A, L, or R")

outFile.close()
