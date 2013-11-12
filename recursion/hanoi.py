#!/usr/bin/env python
# coding: utf-8


"""
递归解决汉诺塔搬运

"""


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print ("moving disk from", fp, "to", tp)

moveTower(1, 'A', 'B', 'C')
