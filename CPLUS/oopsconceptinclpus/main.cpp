#include <iostream>

using namespace std;



int main()
{
    cout << name << endl;
    cout << student02::name << endl;
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
