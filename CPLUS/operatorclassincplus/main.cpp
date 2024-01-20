#include <iostream>

using namespace std;

class MyFirstclass
{
public:
    int a=1;
    void multiply()
    {
        int x,y;
        cout << "\nx:" ;
        cin >> x ;
        cout << "y:" ;
        cin >> y ;
        cout << "\nvalue:" << (x*y) ;
    }
    void sub();
};
void MyFirstclass::sub()
{
    int e,f;
    cin >> e >> f ;
    cout << "\nsub:" << (e-f) ;
}
int addition()
{
    int i,j;
    cout << "\ni:" ;
    cin >> i ;
    cout << "j:" ;
    cin >> j ;
    cout << "\nadd: " << (i+j) ;
}
int main()
{
    MyFirstclass MFC ;
    cout << MFC.a ;
    MFC.multiply();
    addition();
    MFC.sub();
    return 0;
}
