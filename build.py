#!/usr/local/bin/python

import os, re, sqlite3
from bs4 import BeautifulSoup, NavigableString, Tag 

db = sqlite3.connect('build/Framer.docset/Contents/Resources/docSet.dsidx')
cur = db.cursor()

try: cur.execute('DROP TABLE searchIndex;')
except: pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = 'build/Framer.docset/Contents/Resources/Documents'

page = open(os.path.join(docpath,'framerjs.com/docs/index.html')).read()
soup = BeautifulSoup(page)

any = re.compile('.*')
for tag in soup.find_all('a', {'href':any}):
    name = tag.text.strip()

    try:
    	c = tag['class']
    except Exception, e:
    	continue

    if c[0] != "sub-section":
    	print c
    	continue
    
    if len(name) > 0:

        path = tag.attrs['href'].strip()
        
        if not path.startswith("index.html#"):
        	continue

        path = "framerjs.com/docs/" + path

        cur.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)", (name, 'func', path))
        print 'name: %s, path: %s' % (name, path)

db.commit()
db.close()