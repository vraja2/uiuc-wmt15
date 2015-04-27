#!/usr/bin/bash

python score.py tags_testing.json tags.json > yes
/opt/moses/scripts/tokenizer/detokenizer.perl -l en < yes > yes.detok
perl wrap-xml.perl en ~/baseline/test-src.cs.sgm HeyYo < yes.detok > yes.sgm
/opt/moses/scripts/generic/mteval-v13a.pl -r ~/baseline/test-ref.en.sgm -t yes.sgm -s ~/baseline/test-src.cs.sgm
