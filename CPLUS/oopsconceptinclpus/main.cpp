#include <iostream>

using namespace std;

int main()
{
    /*string name;
    cout << "Enter the Name:" ;
    cin >> name ;
    cout << name << endl ;
    fflush(stdin);
    cout << "Enter the Second Name:" ;
    getline(cin,name);
    cout << name << endl;
    */

    string firstname;
    string secondname;
    cin >> firstname >> secondname ;
    cout << firstname+" "+secondname << endl ;

    string fullname = firstname.append(secondname);
    cout << fullname << endl ;

    secondname.push_back('k');
    cout << secondname << endl ;


    firstname.push_back('SS');
    cout << firstname << endl ;
    cout << firstname+" "+secondname << endl ;

    fflush(stdin);
    cin >> fullname ;
    fullname.insert(5, " A ");
    cout << fullname ;

    return 0;
}

/*
#include <iostream>

using namespace std;

namespace student
{
    string name=" Kowsalya " ;
}
namespace student02
{
    string name= "Santhiya" ;
}

using namespace student;

int main()
{
    cout << name << endl;
    cout << student02::name << endl;
    return 0;
}
*/
