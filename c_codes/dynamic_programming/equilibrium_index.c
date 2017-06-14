// you can write to stdout for debugging purposes, e.g.
// printf("this is a debug message\n");

void calculateLeftToRightSum(int dest[], int src[], int N)
{
    int i;
    
    // Dynamic programming to gain cumulative sum
    dest[0] = src[0];
    for(i = 1; i < N; i++)
    {
        dest[i] = dest[i - 1] + src[i];
    }
}

void calculateRightToLeftSum(int A[], int N) 
{
    int i;
    
    for(i = N - 2; i >= 0; i--)
    {
        A[i] = A[i + 1] + A[i];
    }
}

int solution(int A[], int N)
{
    // write your code in C99 (gcc 4.8.2)
    int i = 0;
    
    // Hold place for left to right cumulative sum. 
    // Ww need extra space to hold original references for right to left cumulative sum.
    int *left_to_right_array = (int *) malloc(sizeof(int) * N);
    
    // Calculate left to right sum in cumulative way
    calculateLeftToRightSum(left_to_right_array, A, N);
    
    // Calculate right to left sum in cumulative way
    calculateRightToLeftSum(A, N);
    
    for(i = 0; i < N; i++)
    {
        if (A[i] == left_to_right_array[i])
        {
            return i;   
        }
    }
    
    if(! A[0])
    {
        return 0;    
    }
    
    if(! left_to_right_array[N -1])
    {
        return N-1;
    }
    
    return -1;
}