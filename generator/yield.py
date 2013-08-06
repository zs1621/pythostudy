#!/usr/bin/env python
# coding: utf-8
# 理解步骤: 
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1 # <<<<<<<<<

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 10:
            total += next_prime
        else:
            print(total)
            return

#solve_number_10()
"""
	34: solve_number_10 开始执行
	27: for循环便利 get_primes(3) 
	18: 进入 get_primes
	20: 3是素数
	21：yield 3
	27: 进入solve_number_10 把 返回的 3赋值给 next_prime 
	28: 3 < 10 所以  total = 3 + 2
	23: for循环从get_primes请求下一个值
	22: 注意，此时进入get_primes 从 22行开始  yield会做两件事： 1。会将值传给next()的调用方 2.保存生成器函数的'状态'

"""

def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

print_successive_primes(2)
