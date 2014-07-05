all: .deps/.d
	hfst-lexc apertium-zul.zul.lexc -o .deps/zul.lexc.hfst
	hfst-twolc apertium-zul.zul.twoc -o .deps/zul.twoc.hfst
	hfst-twolc apertium-zul.zul.twol -o .deps/zul.twol.hfst

	hfst-compose-intersect -1 .deps/zul.lexc.hfst -2 .deps/zul.twol.hfst | hfst-invert -o .deps/zul.mor.hfst
	hfst-compose-intersect -1 .deps/zul.mor.hfst -2 .deps/zul.twoc.hfst | hfst-fst2fst -f foma -o .deps/zul.automorf.hfst
	hfst-invert .deps/zul.automorf.hfst -o .deps/zul.autogen.hfst

	hfst-fst2txt .deps/zul.automorf.hfst -o zul.automorf.att
	hfst-fst2txt .deps/zul.autogen.hfst -o zul.autogen.att

	cg-comp apertium-zul.zul.rlx zul.rlx.bin

	lt-comp lr zul.automorf.att zul.automorf.bin 
	lt-comp lr zul.autogen.att zul.autogen.bin 

.deps/.d:
	test -d .deps || mkdir .deps
	touch $@

clean:
	rm *.hfst *.rlx.bin
