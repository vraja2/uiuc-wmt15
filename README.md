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

## Baseline experiment

- Used full Europarl parallel corpus (~600,000 sentences) 
- Tested on News test 2013 

```
test: 17.72 (0.983) BLEU-c ; 18.59 (0.983) BLEU
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
