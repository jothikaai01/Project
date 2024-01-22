#include <iostream>

using namespace std;

class nestedclass
{
public:
     void nestedclass1();

};
class nestedfunction
{
public:
    nestedfunction()
    {
        cout << "Nested the class" ;
    }
};
void nestedclass::nestedclass1()
{
    nestedfunction nsf;
}


int main()
{
    nestedfunction nsf;
    return 0;
}

/*
#include <iostream>

using namespace std;

class functionoverload
{
public:
     void string1()
    {
        string Name;
        cout << "Enter the Name:" ;
        cin >> Name ;
        cout << "\tHello!...." ;
    }
    void string2(string Name)
    {
        cout << "\nName is :" << Name ;
        cout << "\n\tHello!...." << Name ;
    }
    int string3(string Name, int Year)
    {
        cout << "\nMy Name is :" << Name ;
        cout << "\n\tI am Born in....." << Year ;
    }

};

int main()
{
    functionoverload st;
    st.string1();
    st.string2("Santhiya");
    st.string3("Hajeera",1992);
    return 0;
}

*/
/*
#include <iostream>

using namespace std;

class stringclass
{
public:
    stringclass()
    {
        cout << "Enter the Name:" ;
        string Name ;
        cin >> Name ;
        cout << "Hello!....." << Name ;
        int a ;
        cout << "\nEnter case:" ;
        cin >> a;
        switch ( a )
        {
        case 1 :
            cout << " Ammu Welcome to the class\n" ;
            break;
        case 2 :
            cout << " santhiya Welcome to the class\n" ;
            break;
        case 3 :
            cout << " Hajeera Welcome to the class\n" ;
            break;
        }
    }

    stringclass(string a, string b)
    {
        string c;
        c= a+b;
        cout << "concatenated string value is  . " << c;

    }


};

int main()
{
    stringclass stcl;
    stringclass stcl1("Ammu","Kutty");
    return 0;
}

*/
