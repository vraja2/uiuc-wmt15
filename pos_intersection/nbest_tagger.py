import nltk
import re
import sys
import pickle
from collections import defaultdict

reload(sys)
sys.setdefaultencoding("utf-8")

nbest_file = open('./test.output.2.best100')
nbest_lines = nbest_file.readlines()
tag_list = []
parsed_sentences = []
line_num_dict = defaultdict(list)
for line in nbest_lines:
    line_list = line.split()
    line_num = line_list[0]
    start_flag = False  
    parsed_list = []
    for word in line_list:
	matches = re.findall(r"\|[0-9]+\-[0-9]+\|",word)
	if matches:
	   continue
	if start_flag == False and word == "|||":
	   start_flag = True
        elif start_flag == True and word == "|||":
	   start_flag = False
	   break
	elif start_flag == True:
	   parsed_list.append(word)
	else:
	   continue
    line_num_dict[line_num].append(parsed_list)
    parsed_sentences.append(parsed_list)

tag_list = []
for line_num,tagged_sentences in line_num_dict.items():
    curr_tag_list = []
    for sentence in tagged_sentences:
        s = [unicode(word) for word in sentence]
	tagged_sen = nltk.pos_tag(s) 
	sentence_str = ' '.join(sentence)
	curr_tag_list.append([sentence_str,tagged_sen])
    tag_list.append(curr_tag_list)

output_taglist = open('tags.pkl','wb') 
pickle.dump(tag_list,output_taglist)
