#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_STR_LEN     (1000 + 5)
#define MAX_STR_COUNT   (50 + 2)

void* malloc(size_t s);
void free(void *p);

int MOD = 1000000000 + 7;

char Indices[MAX_STR_LEN];
char Compound[MAX_STR_LEN];
int Prev[MAX_STR_LEN];
int Next[MAX_STR_LEN];
int Matrix[MAX_STR_LEN][MAX_STR_LEN];

long mod(long x)
{
    if(x >= 0)  
        return x % MOD;    
    else 
        return x + MOD;
}

void countPals(int n_str)
{
    int diff;
    int r, c;
    
    for(r = 0; r < n_str; r++)
    {
        Matrix[r][r] = 1;    
    }
    
    for (diff = 1; diff < n_str; diff++) 
    {
        for (r = 0; r < n_str - diff; r++) 
        {
            c = r + diff;

            if(Indices[r] == Indices[r + 1] && Indices[c] == Indices[c - 1])
            {
                Matrix[r][c] = mod(Matrix[r + 1][c] + Matrix[r][c - 1] - Matrix[r + 1][c - 1]);
            }
            else if(Indices[r] == Indices[r + 1])
            {
                Matrix[r][c] = Matrix[r + 1][c];             
            }
            else if(Indices[c] == Indices[c - 1])
            {
                Matrix[r][c] = Matrix[r][c -1];
            }
            else
            {
                Matrix[r][c] = 0;    
            }
            
            if(Compound[r] == Compound[c])
            {    
                Matrix[r][c] = mod(Matrix[r][c] + Matrix[r + 1][c -1]);
                
                if(Indices[r] == Indices[r + 1] && Indices[c] == Indices[c - 1])
                {
                    // Calculation is divided into three to prevent possible overflow
                    Matrix[r][c] = mod(Matrix[r][c] + Matrix[r + 1][Prev[c]]);
                    Matrix[r][c] = mod(Matrix[r][c] + Matrix[Next[r]][c - 1]);
                    Matrix[r][c] = mod(Matrix[r][c] + Matrix[Next[r]][Prev[c]]);
                }
                else if(Indices[r] == Indices[r + 1])
                {
                    Matrix[r][c] = mod(Matrix[r][c] + Matrix[Next[r]][c - 1]);
                }
                else if(Indices[c] == Indices[c - 1])
                {
                    Matrix[r][c] = mod(Matrix[r][c] + Matrix[r + 1][Prev[c]]);
                }
                
                // Allow empty string between two indices if they are only in the same or neighbour strings
                if(Indices[r] == Indices[c] || Indices[r] + 1 == Indices[c])
                {    
                    Matrix[r][c] = mod(Matrix[r][c] + 1);
                }
            }
        }
    }
    
    /*
    for(r = 0; r < n_str; r++)
    {
        for(c = 0; c < n_str; c++)
        {
            printf("%d ", Matrix[r][c]);
        }
        printf("\n");
    }*/
}

void calcPrevAndNext(int buffer_len)
{
    int i;
    int n = -1;
    int p = -1;
    
    Prev[0] = p;
    for(i = 1; i < buffer_len; i++)
    {
        if(Indices[i] != Indices[i - 1])
        {
            p = i - 1;
        }
        Prev[i] = p;
    }
    
    Next[buffer_len - 1] = n;
    for(i = buffer_len - 2; i >= 0; i--)
    {
        if(Indices[i] != Indices[i + 1])
        {
            n = i + 1;
        }
        Next[i] = n;
    }
    
    /*
    for(i = 0; i < buffer_len; i++)
    {
        printf("(%d, %d, %d), ", Indices[i], Prev[i], Next[i]);
    }
    printf("\n");
    */
}


int solve(int str_count, char *all_str[])
{
    int i, j;
    int len, buffer_len;
    long result;
    
    if(str_count <= 0)
    {
        return 0;
    }
  
    Indices[0] = 0;
    strcpy(Compound, "_");
    buffer_len = 1;
    for (i = 0; i < str_count; i++)
    {
        strcat(Compound, all_str[i]); 
        len = strlen(all_str[i]);
        for(j = 0; j < len; j++)
        {
            Indices[buffer_len + j] = i + 1;
        }
        buffer_len += len;
    }
    Indices[buffer_len] = i + 1;
    buffer_len++;
    strcat(Compound, "_");
    
    calcPrevAndNext(buffer_len);
    countPals(buffer_len);
    
    return Matrix[0][buffer_len - 1];
}

void readInput()
{
    char buffer[MAX_STR_LEN];
    char *all_str[MAX_STR_COUNT];
    char *cur_str;
    int i, j;
    int no_of_tests;
    int str_count;
    int cur_str_len;
    
    scanf("%d", &no_of_tests);
    for (i = 0; i < no_of_tests; i++)
    {
        scanf("%d", &str_count);
        for(j = 0; j < str_count; j++)
        {
            scanf("%s", buffer);
            cur_str_len = strlen(buffer);           
            cur_str = (char *) malloc(sizeof(char) * (cur_str_len + 1));
            strcpy(cur_str, buffer);
            all_str[j] = cur_str;
        }
        
        printf("%d\n", solve(str_count, all_str));
        
        for(j = 0; j < str_count; j++)
        {
            free(all_str[j]); 
        }
    }
}

int main() 
{
    readInput();
    return 0;
}

/*
*** Example Input: ***
7
2
mweyydiadtlcouegmdbyfwurp
puvhifnuapwyndmhtqvkgkbhtytszotw
4
sjzzszfwtzfpnscguemwrczqxycivdqnkypnxnnpmu
hznoaquudhavrncwfwujpcmiggjmcmkkbnjfeo
kgjgwxtrxingi
uhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarve
1
qfistulg
2
mfgzrnyxryetwzhlnfewczmno
lqatugmdjwgzc
4
koxyjxkatjmpprswkdkobdagw
xsufeesrvncbszcepigpbzuzoootor
skcwbqorvwdrmklfdczatfarqdkelalxzxil
fdvpfpxabqlngdscren
5
ztvvcvrtcmbqlizijdwtuyfrxolsysxlfebpolcmqs
mrfkyunydtmwbexsng
wvroandfqjamz
ttslildlr
oyrpxugiceahgiakevsjoadmkfnkswrawk
1
mcciabzbrskzazjqtlkiqydptpkcsdgcqjshznd



*** Correct Output: ***
90230
266304228
8
1871
124761868
291714766
3278


*/