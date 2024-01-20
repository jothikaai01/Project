#include<stdio.h>
int main()
{
    int a;
    printf("\nEnter the value is a:");
    scanf("%d",&a);
    if(a % 2 == 0)
    {
        printf("Odd Nomber");
    }
    else 
    {
        printf("Even Number");
    }
    return 0;
}