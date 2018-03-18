#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Greetor(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    def greet(self, loud=False):
        if (loud):
            print('Hello,%s' % self.name.upper())
        else:
            print('hello,%s' % self.name)


g = Greetor('Fredmen');
g.greet()
g.greet(True)
