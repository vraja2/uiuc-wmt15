import re
import json
import sys

source = open(sys.argv[1],'r').readlines()
sent_tags = []
for line in source:
    pos_tags = re.findall('POS=.\|', sent)
    pos_tags = [tag[-2] for tag in pos_tags]
    sent_tags.append(pos_tags)
json.dump(sent_tags, open(sys.argv[2],'w'))
