#! /usr/bin/env python
#! -*- coding:utf-8 -*-

# Copyright (c) 2013, Riccardo Iaconelli
# See README.txt for additional licensing information.


# All the tex generation is handled by texcaller: 
# https://github.com/vog/texcaller

class BaseDocTemplate:
    def build(self, flowables, filename=None):
        finaltex = flowables.join('\n')
        