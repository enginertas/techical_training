#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

long tenPow(int i)
{
    static long powers[16] = {
        1, 10, 100, 1000,
        10000, 100000, 1000000, 10000000,
        100000000, 1000000000, 10000000000, 100000000000,
        1000000000000, 10000000000000, 100000000000000, 1000000000000000
    };

    return powers[i];
}

long multiplyMod(long a, long b, long mod) 
{
    long result = 0;
    
    if(a > mod)
    {
        a -= mod;
    }
    if(b > mod)
    {
        b -= mod;
    }
    
    while (b) 
    {
        if (b & 1) 
        {
            result += a;
            if(result > mod)
            {
                result -= mod;
            }            
        }
        b >>= 1; 
        a <<= 1;
        if (a > mod)
        {
            a -= mod;
        }         
    }
    
    return (long) result;
}


long powerMod(long a, long n, long mod) 
{
    long r = 1;
    while (n) 
    {
        if (n & 1) 
        {
            r = multiplyMod(r, a, mod);
        }
        n >>= 1;
        a = multiplyMod(a, a, mod);
    }
    return r;
}

/**
 *  Prime checker for numbers < 2^64
 */
int isPrime(long n) 
{
    int i, j;
    int ok;
    long bit_count, temp, pt;
    static const int base_primes[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23};

    // Trimmed for optimality --- 8 instead of 9    
    for (i = 0; i < 8; i++)
    {
        if(n == base_primes[i])
        {
            return true;
        } 
        else if (! (n % base_primes[i]))
        {
            return false;
        }
    } 

    // Trimmed for optimality --- 19 instead of 23
    if (n < 19)
    {
        return 0;     
    } 
    
    bit_count = 0;
    temp = n - 1;
    while (~temp & 1)
    {
        temp >>= 1;
        bit_count++;        
    }
 
    // Trimmed for optimality --- 8 instead of 9 
    for (i = 0; i < 8; i++) 
    {
        pt = powerMod(base_primes[i], temp, n);
        if (pt == 1) 
        {
            continue;
        }
            
        ok = 0;
        for (j = 0; j < bit_count && !ok; ++j) 
        {
            if (pt == n - 1)
            {
                ok = 1;
            }
            pt = multiplyMod(pt, pt, n);
        }
        
        if (!ok)
        {
            return 0;
        }
    }
    return 1;
}

int countSingleDigitNumbers(long first, long last){    
    int count = 0;
    
    if(first <= 2 && last >= 2){
        count += 1;    
    }
    if(first <= 3 && last >= 3){
        count += 1;    
    }
    if(first <= 5 && last >= 5){
        count += 1;  
    }
    if(first <= 7 && last >= 7){
        count += 1;  
    }
   
    return count;
}
    
int returnProblemIndex(long number) {
    int last_d;
    int index;    
    
    for (index = 0; number; index ++, number /= 10){
        last_d = number % 10;
        if (! (last_d == 2 || last_d == 3 || last_d == 5 || last_d == 7)){
            return index;    
        }
    }
  
    return -1;
}

long roundToUpperPrimeDigitPrime(long number){
    int allowed[4] = {2, 3, 5, 7};
    int p_index;
    int i;
    long cur;
    
    while((p_index = returnProblemIndex(number)) != -1){
        for(cur = number, i = 0; i < p_index; i++){
            cur /= 10;
        }
        cur %= 10;
        
        number -= cur * tenPow(p_index);
        for(i = 0; i < 4; i++){
            if(cur < allowed[i]){
                cur = allowed[i];
                break;
            }
        }        
        if(i == 4){
            cur = 12;
        }
        number += cur * tenPow(p_index);
        
        for(i = 0; i < p_index; i++){
            number /= 10;    
        }
        number *= tenPow(p_index);
        for(i = 0; i < p_index; i++){
            number += 2 * tenPow(i);
        }
    }
    
    if(number % 10 == 2){
        number += 1;
    }
    else if(number % 10 == 5){
        number += 2;
    }
    
    return number;
}  
    
long roundToLowerPrimeDigitPrime(long number)
{
    int allowed[4] = {2, 3, 5, 7};
    int p_index;
    int i;
    long cur;
    long new_digit;
    
    while((p_index = returnProblemIndex(number)) != -1){
        for(cur = number, i = 0; i < p_index; i++){
            cur /= 10;
        }
        cur %= 10;
                
        for(i = 3; i >= 0; i--){
            if(cur > allowed[i]){
                new_digit = allowed[i];
                break;
            }
        }        
        if(i < 0){
            for(i = 0; i < p_index; i++){
                number /= 10;    
            }
            number = (number - 1) * tenPow(p_index);
            for(i = 0; i < p_index; i++){
                number += 7 * tenPow(i);   
            }
        }
        else{
            number -= cur * tenPow(p_index);
            number += new_digit * tenPow(p_index);
            if(cur != new_digit)
            {
                for(i = 0; i < p_index; i++){
                    number /= 10;    
                }
                number *= tenPow(p_index);
                for(i = 0; i < p_index; i++){
                    number += 7 *  tenPow(i);   
                }
            }
        }
    }
    
    return number;  
}
    
void convertLongToResolved(long number, int number_resolved[])
{
    int i;
    int cur_i;
    int number_index[10] = {-1, -1, 0, 1, -1, 2, -1, 3, -1, -1}; 
    
    for(cur_i = 0; number; cur_i++, number /= 10){
        number_resolved[cur_i] = number_index[number % 10];
    }
    for(i = cur_i; i < 20; i++){
        number_resolved[i] = -1;    
    }
}

void incrementPrimeDigitPrime(long *first, int number_resolved[]){
    static int value_gain[4] = {2, 1, 2, 2};
    int i;
    int carry = 0;
    
    carry = 0;
    number_resolved[0] += 2; 
    if(number_resolved[0] > 4){
        number_resolved[0] -= 4;
        carry = 1;
        *first -= 4;
    }
    else
    {
        *first += 4;
    }
    
    for(i = 1; carry; i++){
        number_resolved[i] ++;
        if(number_resolved[i] == 4){
            number_resolved[i] = 0;
            carry = 1;
            *first -= 5 * tenPow(i);
        }
        else{
            carry = 0;
            *first += (value_gain[number_resolved[i]]) * tenPow(i);
        }
    }
}

long solve(long first, long last){
    long count;
    int first_resolved[20];
        
    count = countSingleDigitNumbers(first, last);
    if(first < 10){
        first = 10;
    }
    if(last < 3){
        last = 3;    
    }
    first = roundToUpperPrimeDigitPrime(first);
    last = roundToLowerPrimeDigitPrime(last);
        
    convertLongToResolved(first, first_resolved);
    while(first <= last)
    {
        if(isPrime(first)){
            count++;
        }
        incrementPrimeDigitPrime(&first, first_resolved);
    }
    
    return count;        
}


int main(){
    long first; 
    long last;
    int result;

    while(scanf("%ld %ld", &first, &last) != -1)
    {
        result = solve(first, last);
        printf("[%ld, %ld] --> %d\n", first, last, result);
    }

    return 0;
}