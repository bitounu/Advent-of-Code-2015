def dupa(commands):
    calc = dict()
    results = dict()

    for command in commands:
        (ops, res) = command.split('->')
        calc[res.strip()] = ops.strip().split(' ')

    def calculate(name):
        try:
            return int(name)
        except ValueError:
            pass
        if name not in results:
            ops = calc[name]
            if len(ops) == 1:
                res = calculate(ops[0])
            else:
                op = ops[-2]
                if op == 'AND':
                  res = calculate(ops[0]) & calculate(ops[2])
                elif op == 'OR':
                  res = calculate(ops[0]) | calculate(ops[2])
                elif op == 'NOT':
                  res = ~calculate(ops[1]) & 0xffff
                elif op == 'RSHIFT':
                  res = calculate(ops[0]) >> calculate(ops[2])
                elif op == 'LSHIFT':
                  res = calculate(ops[0]) << calculate(ops[2])
            results[name] = res
        return results[name]

    myA = calculate('a')
#    print "=========== results ===============\n", results
    print "=========== a ===============\n", myA


def parseFile(plik):
    commands = []
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        for line in myfile:
            line = line.rstrip('\r\n')
            if line == '1674 -> b':
                print "line:    ", line
                line = '46065 -> b'
                print "line:    ", line
            commands.append(line)
#    print "=========== commands ===============\n", commands
    dupa(commands)



def check_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.exists(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} not exists".format(x))
    return x

if __name__ == "__main__":
    import argparse, sys, os, re
    from argparse import ArgumentParser

    Druty = {}      # Slownik na nazwy drutow (globalny)
    ARCH = 65535    # najwieksza liczba jaka mozesz niesc drut (16-bitow)

    parser = ArgumentParser(description="Next script for Advent Of Code game")
    parser.add_argument("-i", "--input",
        dest="filename", required=True, type=check_file,
        help="input file for today", metavar="FILE")
    args = parser.parse_args()

    inputfile = args.filename
    parseFile(inputfile)
