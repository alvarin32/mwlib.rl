#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2013, Riccardo Iaconelli
# See README.txt for additional licensing information.


# All the tex generation is handled by texcaller: 
# https://github.com/vog/texcaller

import pickle

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
        string = str('\n'.join(strlist))
        
        if filename:
            self.filename = filename
        #pickle.dump(len(string), open(self.filename, 'w'))
        #open(self.filename, 'w').write(string)
        
        # Save the pdf to self.filename!
    
    
class NextPageTemplate:
    def __init__(self, content):
        self.content = content
    def __str__(self):
        return self.content
    def __repr__(self):
        return self.content