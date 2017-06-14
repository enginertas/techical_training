#include <stdio.h>

#define MAX_RIGHT_BOUND 10000000

int Is_Prime[MAX_RIGHT_BOUND];
int All_Primes[MAX_RIGHT_BOUND];
int All_Primes_End_i = 0;

void findPrimesToSqrt(long right_b)
{
    int i, j;
    
    Is_Prime[0] = 0;
    Is_Prime[1] = 0;
    for(i = 2; i <= right_b; i++)
    {
        Is_Prime[i] = 1;    
    }

    for(i = 2; i * i <= right_b; i++)
    {
        if(Is_Prime[i])
        {
            for(j = i * i; j <= right_b; j += i)
            {
                Is_Prime[j] = 0;    
            }
        }
    }
        
    All_Primes_End_i = 0;
    for(i = 0; i <= right_b; i++)
    {
        if (Is_Prime[i])
        {
            All_Primes[All_Primes_End_i] = i;
            All_Primes_End_i ++;
        } 
    }
}

int main()
{
    int i;
    int rb;

    scanf("%d", &rb);
    findPrimesToSqrt(rb);
    for(i = 0; i < All_Primes_End_i; i++)
    {
        printf("%d\n", All_Primes[i]);
    }

    return 0;
}
