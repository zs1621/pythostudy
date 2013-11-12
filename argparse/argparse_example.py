#!/usr/bin/env python
# coding: utf-8

"""
parser = argparse.ArgumentParser()

 - parser.add_argument
        help: description
        action: 动作 count-参数个数， default-参数默认值, store_true-如果参数指定，赋值 True 或 args.verbose, choice-参数可以选择的值, type-参数的类型
 - parser.parse_args


"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="echos the string you use here", type=int)


parser.add_argument("-v","--verbosity", action="count", help="increase output verbosity")

args = parser.parse_args()

answer = args.square**2

if args.verbosity == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity == 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer
