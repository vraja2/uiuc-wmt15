import json
import sys
import copy

mapping = json.load(open('tags_map.json','r'))
source = json.load(open(sys.argv[1],'r'))
#print len(source)
n_best = json.load(open(sys.argv[2],'r'))
#print len(n_best)
#print "START"
for i in range(len(source)):
    candidates = n_best[i]
    max_cand = (-1, -1)
    sent_len = len(source[i])
    for j,candidate in enumerate(candidates):
        source_sent = copy.deepcopy(source[i])
        num_matches = 0
        for word, tag in candidate[1]:
            tag = mapping[tag]
            if tag in source_sent:
                num_matches += 1
                source_sent.remove(tag)
        if num_matches > max_cand[1]:
            max_cand = (candidates[j][0], num_matches)
    if float(max_cand[1]) / sent_len < .0:
        print candidates[0][0].encode('utf-8')
    else:
        print max_cand[0].encode('utf-8')
    #ratio_correct.append(float(max_cand[1]) / sent_len)
#print ratio_correct
#print sum(ratio_correct) / len(ratio_correct)
