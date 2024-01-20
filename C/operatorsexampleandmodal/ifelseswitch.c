#include<stdio.h>

int main()
{
  int b;
  char operator;
  printf("Enter the 2 or 3 value \t ");
  scanf("%d",&b);
  if( b == 2) 
   {
      int x,y;
      printf("enter the value X :");
      scanf("%d",&x);
      printf("enter the value Y :");
      scanf("%d",&y);
      printf("Select Operator");
      scanf(" %c",&operator);
      switch(operator)
        {
          case '+':
            printf("Addition x+y:%d\t",x+y);
            break;
          case '-':
            printf("Subtraction x-y:%d\t",x-y);
            break;
          case 3:
            printf("Multiplication x*y:%d\t",x*y);
            break;
        }
   }
  else
   {
    int x,y,z,operator;
      printf("enter the value X :");
      scanf("%d",&x);
      printf("enter the value Y :");
      scanf("%d",&y);
      printf("enter the value Z :");
      scanf("%d",&z);
      printf("Select Operator");
      scanf("%d",&operator);
      switch(operator)
      {
        case 1:
          printf("Addition x+y+z:%d\t",x+y+z);
          break;
        case 2:
          printf("Subtraction x-y-z:%d\t",x-y-z);
          break;
        case 3:
          printf("Multiplication x*y*z:%d\t",x*y*z);
          break;
      }
   }
 return 0;
}