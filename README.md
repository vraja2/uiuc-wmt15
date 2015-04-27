# uiuc-wmt15
Submission for WMT 2015

Vignesh Raja and Yisi Liu

#Method

#Results


## Toy experiment

- Used 1000 sentences from Europarl parallel corpus
- Tested on News test 2013

```
test: 2.22 (0.876) BLEU-c ; 2.35 (0.876) BLEU
``` 

## Baseline experiments

- Used full Europarl parallel corpus (~600,000 sentences) 
- Tested on News test 2013 

```
test: 17.72 (0.983) BLEU-c ; 18.59 (0.983) BLEU
```

- Used Common Crawl corpus and News Commentary v10.
- Tested on News test 2013 

```
test: 19.83 (0.982) BLEU-c ; 20.69 (0.982) BLEU
```

## Stem Czech words

- Use hard-stemming length of 6
- Used full Europarl parallel corpus (~600,000 sentences) 
- Tested on News test 2013 

```
test: 17.08 (0.948) BLEU-c ; 17.88 (0.948) BLEU
```

## Use Morfessor during pre-processing to extract morphemes of Czech words 

- Trained Morfessor on toy data (1000 Czech sentences from Europarl) 
- Trained Moses on 1000 sentences from Europarl
- Tested on News test 2013

```
test: 1.00 (1.489) BLEU-c ; 1.06 (1.489) BLEU
```

- Trained Morfessor on full Europarl Czech corpus 
- Trained Moses on 1000 sentences from Europarl
- Tested on News test 2013

```
test: 1.02 (1.253) BLEU-c ; 1.09 (1.253) BLEU
```

- Trained Morfessor on full Europarl Czech corpus
- Trained Moses on full Europarl parallel corpus
- Tested on News test 2013

```
test: 15.74 (1.071) BLEU-c ; 16.48 (1.071) BLEU
```

## Score 100-best list with pos intersection
- Trained on the full Europarl data plus Common Crawl and Commentary
- Tested on News test 2014
- Score 100 outputs for each source sentence and output the one with the largest number of intersection
```
NIST score = 6.2859  BLEU score = 0.1904
```

## HOWTO translate using our model

- Tokenize: 
```
perl -ne 'print $1."\n" if /<seg[^>]+>\s*(.*\S)\s*<.seg>/i;' < SRC.sgm > SRC.tok
```
- Lowercase: 
```
/opt/moses/scripts/tokenizer/lowercase.perl < SRC.tok > SRC.input
```
- Filter the model into memory: You need to first wget https://raw.githubusercontent.com/moses-smt/mosesdecoder/master/scripts/training/filter-model-given-input.pl and then change line 118 to the correct path. Then run: 
```
perl filter-model-given-input.pl FILTERED_DIR ~/DIR_YOU_TRAINED_YOUR_MODEL/tuning/moses.tuned.ini.* SRC.input
```
- Run moses: 
```
/opt/moses/bin/moses -f FILTERED_DIR/CONFIG_FILE -i THE_FILE_IN_FILTERED_DIR > OUTPUT_FILE
```
