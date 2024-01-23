#include <iostream>

using namespace std;

class returnornotreturn
{
private:
  int a;

public:
    string name;
    void voidfunction(int b)
    {
        a=b;
    }
    int intfunction()
    {
        return a;
    }

};

int main()
{
    returnornotreturn ror;
    string name;
    cout << "Your Name is :" ;
    cin >> ror.name ;
     cout << "\n voidfunction: " ;
    ror.voidfunction(200);
    cout << "\n intfunction: " ;
    cout << ror.intfunction();

    return 0;
}

/*
#include <iostream>

using namespace std;

class accessspecifier
{
private:
  int a=25;
protected:
    int b=30;
public:
    int c;
    void functionprint()
    {
        int d;
        d=a;
        cout << "\nPrivate access:" << d ;
        int e;
        e=b;
        cout << "\nProtected access:" << e ;

    }

};

int main()
{
    accessspecifier acs;
    acs.c=35;
    cout << "Public access:" << acs.c;
    acs.functionprint();
    return 0;
}

*/
