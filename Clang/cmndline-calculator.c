#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int result;
    result = a + b;

    printf("Result is: %d\n", result);
    return 0;
}