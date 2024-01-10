all: corpus_ambig.txt

ap_ops.txt: lab2ap.py 2010.07.17.WordListLabelled.txt
	cat 2010.07.17.WordListLabelled.txt | python3 lab2ap.py > $@

conv_todo_ana.txt: ap_ops.txt
	grep '??' $< > $@ || touch $@

conv_todo_tag.txt: ap_ops.txt
	sed -E 's/[<>]/\n/g' $< | grep '??' | sort | uniq -c | sort -nr > $@

corpus_ambig.txt: make_ambig_corpus.py ap_ops.txt 2010.07.17.ZuluSentencesUntagged.txt
	python3 $^ > $@
