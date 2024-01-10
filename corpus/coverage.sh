#!/bin/bash

TMPCORPUS=ukwabelana_text.txt
#TMPCORPUS=../../LING-L645/wiki.txt
TMPPARADE=parade.txt
#TMPPARADE=zw_coverage.txt

cat $TMPCORPUS | apertium -d .. zul-morph | apertium-cleanstream -n > $TMPPARADE

cat $TMPPARADE | grep '\*' | sort | uniq -c | sort -rn | head -n30

TOTAL=`grep -v '^$' $TMPPARADE | wc -l`
KNOWN=`grep -v '^$' $TMPPARADE | grep -v '\*' | wc -l`
UNKNOWN=`grep -v '^$' $TMPPARADE | grep '\*' | wc -l`

PERCENTAGE=`echo $KNOWN/$TOTAL | calc -p | sed 's/[\s\t]//g'`

echo "coverage: $KNOWN / $TOTAL ($PERCENTAGE)"
echo "remaining unknown forms: $UNKNOWN"
