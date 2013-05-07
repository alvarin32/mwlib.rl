#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2013, Riccardo Iaconelli
# See README.txt for additional licensing information.

# Clone Reportlab's API and provide drop-in LaTeX substitutes
# which can be simply print()'d out.

# All the tex generation is handled by texcaller: 
# https://github.com/vog/texcaller

import texcaller

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
        return texcaller.escape_latex(self.text)
    def __repr__(self):
        return self.__str__()
      
class Table(SimpleElement):
    def __init__(self, tabledata):
        #assert 0
        content = ''
        rowsCount = 0
        for row in tabledata:
            escaped_row = []
            for cell in row:
                escaped_row.append(texcaller.escape_latex(cell))
            content += u" & ".join(escaped_row)
            content += u'\\\\ \\hline \n'
            rowsCount = max(rowsCount, len(row))
        #assert 0
            
        self.text = r"\begin{tabular}{|"
        self.text += u"c|"*rowsCount
        self.text += u"}\\hline\n"
        self.text += content
        self.text += r"\end{tabular}"
    def __str__(self):
        return self.text
        
class ListItem(SimpleElement):
    def __init__(self, text, caption=None):
        self.text = text
        #self.text = "prova"
        self.caption = caption
    def __str__(self):
        if (self.caption):
            #return r"\item[%(c)s] %(t)s" % {'c': self.caption, 't': self.text}
            return ""
        else:
            return u"\\item %s \\\\" % texcaller.escape_latex(self.text) # {'t': self.text} # texcaller.escape_latex(u"%r" % self.text)}
            
class List(SimpleElement):
    def __init__(self, items):
        self.items = items
        #for i in items:
            
        self.text = "\n"
        it = []
        for el in items:
            it.append(u"%s" %el)
        self.text += r"\begin{itemize}"
        self.text += u"\n".join(it)
        self.text += r"\end{itemize}"
        self.text += "\n"
        #assert 0
    def __str__(self):
        return self.text    
            
class Flowable(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class Preformatted(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class Figure(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class FiguresAndParagraphs(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class SmartKeepTogether(SimpleElement):
    def __init__(self, text, style, bulletStyle=None):
        SimpleElement.__init__(self, text)
        
class MathElement(SimpleElement):
    def __init__(self, text, displayStyle=False, environment=None):
        SimpleElement.__init__(self, text)
        self.displayStyle = displayStyle
        self.environment = environment
        
    def __str__(self):
        if (self.environment):
            return "\\begin{%(env)s}%(text)s\\end{%(env)s}" % \
                        {'env': self.environment, 'text': self.text}
                        
        if (self.displayStyle):
            return "$$" + self.text + "$$"
        else:
            return "$" +self.text + "$"
        
class TocEntry(SimpleElement):
    ''' valid lvl values
        chapter ==> \chapter
        group ==> \section
        article ==> \subsection
    '''
    def __init__(self, txt, lvl=None, bulletStyle=None):
        SimpleElement.__init__(self, txt)
        
    def __str__(self):
        if (self.lvld == 'chapter'):
            return '\chapter{%s}' % self.text
        elif (self.lvld == 'group'):
            return '\subsection{%s}' % self.text
        elif (self.lvld == 'article'):
            return '\section{%s}' % self.text
        
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