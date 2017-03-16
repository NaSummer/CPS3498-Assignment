#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>

int main()
{
    time_t timep;
    char s[30];

    time(&timep);

    strcpy(s,ctime(&timep));

    printf("%s\n", s);
}