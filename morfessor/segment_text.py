import sys
import morfessor

io = morfessor.MorfessorIO(encoding='ISO_8859-2')
model = io.read_any_model('full_model.segm')

stdin = sys.stdin

for line in stdin:
    out = ''
    for word in line.split():
        out += ' '.join(model.viterbi_segment(word)[0])+' '
    print out
