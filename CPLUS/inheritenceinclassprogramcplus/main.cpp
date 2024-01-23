#include <iostream>

using namespace std;

// bass class
class classno1
{
public :
    int a=10;
    void functioncl1()
    {
        cout << "\nIn A value" << endl ;
    }
};

class classno2
{
public :
    int b=15;
    void functioncl2()
    {
        cout << "\nIn B value" << endl ;
    }
};

// child class
class classno3 : public classno1 , public classno2
{

};


int main()
{
    classno3 cl3;
    cout << cl3.a ;
    cl3.functioncl1();
    cout << cl3.b;
    cl3.functioncl2();
    return 0;
}
