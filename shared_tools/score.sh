#!/usr/bin/bash

python score.py tags.cs.json tags_2015.json > yes
echo "done 1"
/opt/moses/scripts/tokenizer/detokenizer.perl -l en < yes > yes.detok
echo "done 2"
perl wrap-xml.perl en /data/parallel/test/newstest2015-csen-src.cs.sgm HeyYo < yes.detok > yes.sgm
echo "done 3"
#/opt/moses/scripts/generic/mteval-v13a.pl -r ~/baseline/test-ref.en.sgm -t yes.sgm -s ~/baseline/test-src.cs.sgm
