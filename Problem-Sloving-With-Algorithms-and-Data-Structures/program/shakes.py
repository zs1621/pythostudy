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
    goal = "methinks it is like a weasel"
    i = 0
    fs = generate(27)
    a = score(fs, goal)
    bs = fs 
    hs = a
    s = a
    while s != 1:
        print s
        gs = generate(27)
        ns = score(gs, goal)
        if ns > s:
            hs = ns    
            bs = gs
        if i / 1000 >= 1:
            print s, bs
        i = i + 1
        s = ns

main()


