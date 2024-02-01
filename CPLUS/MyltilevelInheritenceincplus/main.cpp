#include <iostream>

using namespace std;


class shop
{
public :
    string name;
     void dress ()
    {
        string dname;
        cout << "Dress Name:" ;
        cin >> dname ;
    }

};
//derive class (child class)
class shirt : public  shop
{
public :

    void colour ()
    {
        cout << "White Colour " << endl ;
    }
    void sizeofdress ()
    {
        cout << "ThirtyEight" << endl ;
    }

};
// child class
class kurthi : public  shop
{
public :

    void colour ()
    {
        cout << "Red Colour" << endl ;
    }
    void sizeofdress ()
    {
        cout << "ThirtySix" << endl ;
    }


};

/*
int addition()
{
    int a,b,c;
    a=10;
    b=15;
    c=a+b;
    cout << "Addition value is :" << (a+b) ;
}
*/

int main()
{

    string name ;
    cout << "Shop Name:" ;
    cin >> name ;

    shirt st;
    st.dress ();


    st.colour ();
    st.sizeofdress ();
    cout << " shitclass is end" << endl ;

    st.dress ();
    kurthi kt;
    kt.colour ();
    kt.sizeofdress ();
    cout << " kurthi class is end" << endl ;
    /*
    addition();
    */

    return 0;
}

