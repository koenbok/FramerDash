update:
	rm -Rf build
	mkdir -p build/Framer.docset/Contents/Resources/Documents/
	# curl http://framerjs.com/docs/index.html > build/Framer.docset/Contents/Resources/Documents/index.html
	
	mkdir -p build/Framer.docset/Contents/Resources/Documents/framerjs.com
	cd build/Framer.docset/Contents/Resources/Documents; wget -E -H -k -K -p http://framerjs.com/docs/index.html
	rm -Rf build/Framer.docset/Contents/Resources/Documents/framerjs.com/static/fonts
	rm -Rf build/Framer.docset/Contents/Resources/Documents/framerjs.com/static/images
	rm -Rf build/Framer.docset/Contents/Resources/Documents/framerjs.com/static/js
	rm -Rf build/Framer.docset/Contents/Resources/Documents/ajax.googleapis.com

	echo "nav.top {display: none}" >> build/Framer.docset/Contents/Resources/Documents/framerjs.com/static/css/style.css
	echo ".sidebar {display: none}" >> build/Framer.docset/Contents/Resources/Documents/framerjs.com/static/css/style.css

build:
	cp Info.plist build/Framer.docset/Contents/Info.plist
	python build.py

.PHONY: build