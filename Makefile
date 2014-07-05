all:
	hfst-lexc apertium-zul.zul.lexc -o zul.lexc.hfst
	hfst-twolc apertium-zul.zul.twoc -o zul.twoc.hfst
	hfst-twolc apertium-zul.zul.twol -o zul.twol.hfst

	hfst-compose-intersect -1 zul.lexc.hfst -2 zul.twol.hfst | hfst-invert -o zul.mor.hfst

	hfst-compose-intersect -1 zul.mor.hfst -2 zul.twoc.hfst | hfst-fst2fst -O -o zul.automorf.hfst

	cg-comp apertium-zul.zul.rlx zul.rlx.bin

clean:
	rm *.hfst *.rlx.bin
