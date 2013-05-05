#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2013, Riccardo Iaconelli
# See README.txt for additional licensing information.

# Clone Reportlab's API and provide drop-in LaTeX substitutes
# which can be simply print()'d out.

# All the tex generation is handled by texcaller: 
# https://github.com/vog/texcaller

class Paragraph:
    def __init__(self, text, style, bulletStyle=None):
        self.text = text
        self.style = style
        self.bulletStyle = bulletStyle
    def __repr__(self):
        return self.text
      
class HRFlowable:
  
    def __init(self, width=1,color=1,thickness=1,lineCap=1):
        return
      
    def __repr__(self):
        return self.text