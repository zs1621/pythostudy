#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Rhapsodyzs
#   E-mail  :   zs1213yh@gmail.com
#   Date    :   14/09/28 15:26:53
#   Desc    :  defineFunction - self Check 
#
import random

def generate(strlen):
    commonstring = "abcdefghijklmnopqrstuvwxyz "
    news = ""
    for i in range(strlen):
        news = news + commonstring[random.randint(0, 26)]
    return news
        
def score(newstring, oldstring):
    new = newstring
    old = oldstring
    score = 0
    for i in range(27):
        if new[i] == old[i]:
            score += 1
    return float(score) / 27

def main():
    targetString = "methinks it is like a weasel"
    stringGenerate = generate(27)
    stringScore = score(stringGenerate, targetString)
    string = stringGenerate
    newScore = stringScore
    i = 0
    while newScore != 1:
        i = i + 1
        newGenerate = generate(27)
        if ( score(newGenerate, targetString) > newScore):
            newScore = score(newGenerate, targetString)
            string = newGenerate
        else:
            print newGenerate, "fesfef"

        if ( i % 1000 == 0):
            print i, string, newScore




main()


