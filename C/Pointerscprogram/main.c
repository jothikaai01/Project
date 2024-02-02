#include <stdio.h>
#include <stdlib.h>

int main()
{
    char n[10] = "Jothika" ;
    printf("Value of a : %s\n",n);
    printf("Address of a : %p\n",&n);
    printf("------------------\n");

    char *p= "Jothika" ;
    printf("Value of p : %p\n",p);
    printf("Address of p : %p\n",&p);
    printf("Value stored address p : %s\n",p);
    printf("------------------\n");

    char **q="Jothika";
    printf("Value of q : %p\n",q);
    printf("Address of q : %p\n",&q);
    printf("Value stored address (p)q : %s\n",q);
    printf("------------------\n");

    char ***r="Jothika";
    printf("Value of r : %p\n",r);
    printf("Address of r : %p\n",&r);
    printf("Value stored address (p)(q)r : %s\n",r);
    printf("------------------\n");

    char *s="Jothika";
    printf("Value of s : %p\n",s);
    printf("Address of s : %p\n",&s);
    printf("Value stored address (p)(q)(r)s : %s\n",s);

    return 0;
}

/*
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=2;
    printf("Value of a : %d\n",a);
    printf("Address of a : %p\n",&a);
    printf("------------------\n");

    int *p=&a;
    printf("Value of p : %p\n",p);
    printf("Address of p : %p\n",&p);
    printf("Value stored address p : %d\n",*p);
    printf("------------------\n");

    int **q=&p;
    printf("Value of q : %p\n",q);
    printf("Address of q : %p\n",&q);
    printf("Value stored address (p)q : %d\n",**q);
    printf("------------------\n");

    int ***r=&q;
    printf("Value of r : %p\n",r);
    printf("Address of r : %p\n",&r);
    printf("Value stored address (p)(q)r : %d\n",***r);
    printf("------------------\n");

    int *s=&a;
    printf("Value of s : %p\n",s);
    printf("Address of s : %p\n",&s);
    printf("Value stored address (p)(q)(r)s : %d\n",*(int*)s);
    return 0;
}
*/
