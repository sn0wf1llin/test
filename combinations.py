#!/usr/bin/python

from itertools import combinations as comb
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits
import argparse


def usage():
    print("Usage: {} [ -al | -au | -a | -d | -hex | -oct ] -n 10".format(__file__))
    exit(1)


def make_symbols_set(args):
    sset = set()
    if args.letters:
        sset.add(ascii_letters)
    else:
        if args.lowercase:
            sset.add(ascii_lowercase)

        if args.uppercase:
            sset.add(ascii_uppercase)

    if args.digits:
        sset.add(digits)

    if args.hexdigits:
        sset.add(hexdigits)

    if args.octdigits:
        sset.add(octdigits)

    return sset


def generate(args):
    sset = make_symbols_set(args)
    n = int(args.n)

    scombinations = comb(''.join(str(i) for i in sset), n)

    if args.w is not None:
        with open(args.w, 'a') as f:
            for i in scombinations:
                f.write(''.join(i) + '\n')
    else:
        for i in scombinations:
            print(''.join(i))


def main():
    parser = argparse.ArgumentParser(description='Process combinations')
    parser.add_argument('--ascii-lowercase', '-al', dest='lowercase', action='store_true')
    parser.add_argument('--ascii-uppercase', '-au', dest='uppercase', action='store_true')
    parser.add_argument('--ascii-letters', '-a', dest='letters', action='store_true')
    parser.add_argument('--digits', '-d', dest='digits', action='store_true')
    parser.add_argument('--hexdigits', '-hex', dest='hexdigits', action='store_true')
    parser.add_argument('--octdigits', '-oct', dest='octdigits', action='store_true')
    parser.add_argument('-n', dest='n', action='store', default=0)
    parser.add_argument('-w', dest='w', action='store', default=None)

    args = parser.parse_args()
    if args.n is None or not (args.lowercase or args.uppercase or args.letters or args.digits or args.hexdigits or args.octdigits):
        usage()
        exit()

    generate(args)

main()
