import sys
import re

if sys.argv[1] == 'sgm':
    source = open('test-src.cs.sgm')
    stemmed = open('stemmed.test-src.cs','a')
    for i,line in enumerate(source):
        sent = re.findall('>.+<', line)
        if sent == []:
            continue
        else:
            sent = sent[0][1:-1]
        sent = sent.decode('utf-8')
        words = sent.split()
        stemmed_sent = ' '.join([word[:6].encode('utf-8') for word in words])
        if i < 10:
            print stemmed_sent
        stemmed.write(stemmed_sent + '\n')
    stemmed.close()
else:
    source = open(sys.argv[1]).readlines()
    #stemmed = open(sys.argv[2],'a')
    for i, line in enumerate(source):
        line = line.decode('utf-8')
        words = line.split()
        stemmed_words = [word[:6].encode('utf-8') for word in words]
        print ' '.join(stemmed_words)
    #stemmed.close()
