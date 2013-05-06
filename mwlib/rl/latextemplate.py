#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2013, Riccardo Iaconelli
# See README.txt for additional licensing information.


# All the tex generation is handled by texcaller: 
# https://github.com/vog/texcaller

import texcaller

#\usepackage[cm]{fullpage}
#\usepackage[utf8]{inputenc}
basetempl = r"" \
r"\documentclass[a4paper,10pt]{article}" \
r'' \
r'\usepackage[italian]{babel}' \
r'\usepackage[utf8]{inputenc}' \
r'' \
r'\title{%(title)s}'\
r'\begin{document}' \
'\\maketitle \n'\
r'%(content)s \end{document}'

class BaseDocTemplate:
    def __init__(self, filename, topMargin=0, leftMargin=0, rightMargin=0, bottomMargin=0):
        self.filename = filename
        self.templates = []
    def addPageTemplates(self, pageTemplate):
        self.templates.append(pageTemplate)
    def build(self, flowables, filename=None):
        # print printable flowables
        strlist = []
        for el in flowables:
            try:
                strlist.append(str(el))
            except AttributeError:
                next
        content = str('\n'.join(strlist))
        content += '\n'
        content = basetempl % {'content': content, 'title': 'FIXME Title'}
        
        
        pdf, info = texcaller.convert(content, 'LaTeX', 'PDF', 5)

        
        if filename:
            self.filename = filename
        open(self.filename, 'w').write(pdf)
        
        # Save the pdf to self.filename!
    
    
class NextPageTemplate:
    def __init__(self, content):
        self.content = content
    def __str__(self):
        return self.content
    def __repr__(self):
        return self.content