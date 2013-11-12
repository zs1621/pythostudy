#!/usr/bin/env python
# coding: utf-8


"""

找零钱

"""

li = [1, 5, 10, 20, 50, 100]
def recmy(a):
    i = 0
    j = 0
    m = 0
    n = 0
    x = 0
    y = 0
    while a >= li[5]:
        a = a - li[5]
        i = i + 1
    while a >= li[4]:
        a = a - li[4]
        j = j + 1
    while a >= li[3]:
        a = a - li[3]
        m = m + 1
    while a >= li[2]:
        a = a - li[2]
        n = n + 1
    while a >= li[1]:
        a = a - li[1]
        x = x + 1
    while a >= li[0]:
        a = a - li[0]
        y = y + 1
    print i,j,m,n,x,y

#recmy(9)

def recMC(coinValueList,change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList,change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

#print(recMC([1,5,10,25],63))
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()
