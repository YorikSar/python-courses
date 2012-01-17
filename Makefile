
.PHONY: page

page: .html/index.html

git: page
	cd .html; git commit -am "Update to master branch" && git push

.html/index.html: slides.rst | .html
	rst2s5.py --theme small-white $^ $@

.html:
	git clone -s -b gh-pages . .html
