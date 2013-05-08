#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2013, Riccardo Iaconelli
# See README.txt for additional licensing information.


# All the tex generation is handled by texcaller: 
# https://github.com/vog/texcaller

import texcaller

#\usepackage[cm]{fullpage}
#\usepackage[utf8]{inputenc}

# I can't seem to support chinese
# r'\usepackage[BoldFont,SlantFont,CJKsetspaces,CJKchecksingle]{xeCJK} \setCJKmainfont[BoldFont=SimHei]{SimSun}',

basetempl = [r"",
r"\documentclass[a4paper,10pt]{article}",
r'',
r'\usepackage[italian]{babel}',
r'\usepackage[utf8x]{inputenc}',
r'\usepackage{eurosym}',
r'',
r'\title{%(title)s}',
r'\begin{document}',
'\\maketitle ',
r'%(content)s \end{document}',
r''
]

basetempl = '\n'.join(basetempl)

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
                strlist.append("%s" %el)
            except AttributeError:
                next
        content = '\n'.join(strlist)
        content += u'\n'
        
        content = basetempl % {'content': content, 'title': 'FIXME Title'}
        
        #content = content.encode("utf8")
        #assert 0
        pdf, info = texcaller.convert(content, 'LaTeX', 'PDF', 5)
        
        if filename:
            self.filename = filename
        open(self.filename, 'w').write(pdf)
        #open(self.filename+'.log', 'w').write(info)
        open(self.filename+'.tex', 'w').write(content.encode("utf8"))
        
        # Save the pdf to self.filename!
    
    
class NextPageTemplate:
    def __init__(self, content):
        self.content = content
    def __str__(self):
        return self.content
    def __repr__(self):
        return self.content