#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2013, Riccardo Iaconelli
# See README.txt for additional licensing information.

# Clone Reportlab's API and provide drop-in LaTeX substitutes
# which can be simply print()'d out.

# All the tex generation is handled by texcaller: 
# https://github.com/vog/texcaller

class SimpleElement:
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.__str__()

class Paragraph(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        self.style = style
        self.bulletStyle = bulletStyle
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.__str__()
      
class Figure(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class FiguresAndParagraphs(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class SmartKeepTogether(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class TocEntry(SimpleElement):
    def __init__(self, txt, lvl=None, bulletStyle=None):
        SimpleElement.__init__(self, txt)
        
class DummyTable(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class HRFlowable:
    def __init(self, width=1,color=1,thickness=1,lineCap=1):
        self.text = 'HR'
        return
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.__str__()