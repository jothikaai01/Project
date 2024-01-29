#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b;
    float c;
    int z;
    int y;
    printf("Enter the Value A is :");
    scanf("%d",&a);
    printf("Enter the Value B is :");
    scanf("%d",&b);
    addition(a,b);
    subtraction(a,b);
    multiplication(a,b);
    division(a,b);
    modulus(a,b);
    increment(a,b);
    decrement(a,b);
    assign(a,b);
    addassign(a,b);
    subassign(a,b);
    divassign(a,b);
    multiplyassign(a,b);
    equalto(a,b);
    notequalto(a,b);
    greaterthan(a,b);
    lessthan(a,b);
    greaterthanequal(a,b);
    lessthanequal(a,b);
    AND(a,b);
    OR(a,b);
    NOT(a,b);
    return 0;
}
int addition(a,b)
{
    int z=a+b;
    printf("Addition Value is:%d\n",z);
}
int subtraction(a,b)
{
    int z=a-b;
    printf("Subtraction Value is:%d\n",z);
}
int multiplication(a,b)
{
    int z=a*b;
    printf("Multiplication Value is:%d\n",z);
}
int division(a,b)
{
    float c=(float)a/b;
    printf("Division Value is:%f\n",c);
}
int modulus(a,b)
{
    int z=b%a;
    printf("Modulus Value is:%d\n",z);
}
int increment(a,b)
{
    a++;
    printf("Increment Value is:%d\n",a);
}
int decrement(a,b)
{
    b--;
    printf("Decrement Value is:%d\n",b);
}
int assign(a,b)
{
    int x,y;
    x=3;
    printf("Assign Value is:%d\n",x=y);
}
int addassign(a,b)
{
    a+=3;
    printf("Addassign Value is:%d\n",a);
}
int subassign(a,b)
{
    b-=2;
    printf("Subassign Value is:%d\n",b);
}
int divassign(a,b)
{
    b/=2;
    printf("Divassign Value is:%d\n",b);
}
int multiplyassign(a,b)
{
    a*=2;
    printf("Multiplyassign Value is:%d\n",a);
}
int equalto(a,b)
{
    a==b;
    printf("Equalto Value is:%d\n",a==b);
}
int notequalto(a,b)
{
    a!=b;
    printf("Notequalto Value is:%d\n",a!=b);
}
int greaterthan(a,b)
{
    int z;
    while (z=a>4)
    {
        printf("Greaterthan Value is:%d\n",z);
        return 0;
    }
}
int lessthan(a,b)
{
    int z;
    while (z=b<4)
    {
        printf("Lessthan Value is:%d\n",b);
        return 0;
    }
}
int greaterthanequal(a,b)
{
    printf("Greaterthanequal Value is:%d\n",a>=6);
}
int lessthanequal(a,b)
{
    printf("Lessthanequal Value is:%d\n",b<=6);
}
int AND(a,b)
{
        printf("AND Value is:%d\n",a>4 && b<7);
}
int OR(a,b)
{
    printf("OR Value is:%d\n",a<6 || b>4);
}
int NOT(a,b)
{
    printf("NOT Value is:%d\n",!(a>4 && b<7));
}
