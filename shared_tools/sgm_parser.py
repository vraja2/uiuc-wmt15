#usage: python sgm_parser.py input output

import re, sys

source = open(sys.argv[1], 'r').readlines()
output = open(sys.argv[2], 'a')
for line in source:
    sent = re.findall('>.+<', line)
    if sent != []:
        output.write(sent[0][1:-1]+'\n')
