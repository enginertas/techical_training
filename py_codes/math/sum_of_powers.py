#!/usr/bin/env python

MOD = 10**9 + 9
MAX_POWER = 1005


def calculateFactorials():
    factorial = [1] * MAX_POWER
    for i in xrange(2, MAX_POWER):
        factorial[i] = (factorial[i - 1] * i) % MOD
        
    return factorial


def modularInverse(n):
	return pow(n, MOD - 2, MOD)


def modularDivision(n, k):
    return (n * modularInverse(k)) % MOD
 
    
def modularCombination(n, k):
	return modularDivision(factorial[n], factorial[k] * factorial[n-k])


def calculateBernoulliNumbers():
    bernoulli = [0] * MAX_POWER
    
    tmp = []
    for m in xrange(MAX_POWER):
        tmp.append(modularDivision(1, 1 + m)) 
        for j in range(m, 0, -1):
            tmp[j - 1] = (j * (tmp[j - 1] - tmp[j])) % MOD
        bernoulli[m] = tmp[0]    
        m += 1
        
    return bernoulli
    
    
def solve(n, k):
    if n <= 2:
        return 0
    
    total_sum = 0
    for i in xrange(k + 1):
        total_sum = (total_sum + modularCombination(k + 1, i) * bernoulli[i] * pow(n - 1, k + 1 - i, MOD)) % MOD
        
    return (modularDivision(total_sum, k + 1) - 1) % MOD
    
    
def readInput():   
    q = int(raw_input().strip())
    for i in xrange(q):
        n, k = map(int, raw_input().strip().split())
        print solve(n, k)
        

if __name__ == "__main__":
    bernoulli = calculateBernoulliNumbers()
    factorial = calculateFactorials()
    readInput()
   
