#include <iostream>

using namespace std;

int main()
{
    int Value1,Value2,Total,Operator;
    cout << "Enter the FirstValue:";
    cin >> Value1;
    cout << "Enter the FirstValue:";
    cin >> Value2;
    cout << "Enter Operator:";
    cin >> Operator;
    switch (Operator)
    {
    case 1:
        Total=Value1+Value2;
        cout << "Addition Values:"<<Total;
        break;
    case 2:
        Total=Value1-Value2;
        cout << "Subtraction Values:"<<Total;
        break;
    case 3:
        Total=Value1*Value2;
        cout << "Multiplication Values:"<<Total;
        break;
    case 4:
        Total=Value1/Value2;
        cout << "Division Values:"<<Total;
        break;
    case 5:
        Total=Value1%Value2;
        cout << "Modulas Values:"<<Total;
        break;
    case 6:
        Value1++;
        Value2++;
        cout << "Increment Values:"<<Value1<<Value2;
        break;
    case 7:
        Value1--;
        Value2--;
        cout << "Decrement Values:"<<Value1<<Value2;
        break;
    case 8:
        Value1+=2;
        Value2-=1;
        cout << "Add assign Values:"<<Value1<<endl;
        cout << "Sub assign Values:"<<Value2<<endl;
        break;
    case 9:
        Value1*=2;
        Value2/=2;
        cout << "Multiply assign Values:"<<Value1<<endl;
        cout << "div assign Values:"<<Value2<<endl;
        break;


    }
    return 0;
}
