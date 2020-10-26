//Program to find the given number is even or odd.
#include <iostream>
using namespace std;
int main()
{
    int x;
    cout << "Enter an integer: ";
    cin >> x; //Taking input from user
   
    //To Check if the number is even or odd 
    
    if ( x % 2 == 0){
        cout << x <<" "<< " is even.";
        }
    else{
        cout << x <<" "<< " is odd.";
        }
}
