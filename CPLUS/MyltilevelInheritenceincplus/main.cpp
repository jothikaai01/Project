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

    return 0;
}
