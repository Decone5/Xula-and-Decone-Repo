#include <stdio.h>
#include <windows.h>
#include "headers/xunix.h"

int main(int argc, char const *argv[])
{
    system("@echo off");
    char input[250];
    while (1)
    {
        printf("%s", user);
        scanf("%s", input);
        system(input);
        printf("\n");
        printf("%s Executed %s.", user, input);
        
    }
    
    return 0;
}
