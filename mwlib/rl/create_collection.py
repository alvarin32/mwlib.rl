#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2007, PediaPress GmbH
# See README.txt for additional licensing information.

import optparse
import sys

from mwlib import metabook

def main():
    optparser = optparse.OptionParser(usage="%prog [-o OUTPUT] [-t TITLE] [-s SUBTITLE] ARTICLE [...]")
    optparser.add_option("-o", "--output", help="write output to file OUTPUT")
    optparser.add_option("-t", "--title", help="use given TITLE")
    optparser.add_option("-s", "--subtitle", help="use given SUBTITLE")
    options, args = optparser.parse_args()

    if not args:
        sys.exit('No article given.')

    title = None
    if options.title:
        title = unicode(options.title, 'utf-8')
    subtitle = None
    
    if options.subtitle:
        subtitle = unicode(options.subtitle, 'utf-8')
        
    mb = metabook.MetaBook(title=title, subtitle=subtitle)
    mb.addArticles([unicode(article, 'utf-8') for article in args])
    
    f = open(options.output, 'w') if options.output else sys.stdout
    f.write(mb.dumpJson())
    
if __name__ == '__main__':
    main()
