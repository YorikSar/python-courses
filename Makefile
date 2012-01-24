
.PHONY: page git

page: .html/index.html

git: page
	cd .html;\
		if [ "$$(git status -s)" ]; then \
			git commit -am "Update to master branch" && git push; \
		fi

.html/index.html: slides.rst | .html
	rst2s5.py --theme small-white $^ $@

.html:
	git clone -s -b gh-pages . .html
