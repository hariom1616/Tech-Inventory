#include <iostream>
#include <algorithm>
using namespace std;

string reverseString(string str) {
    reverse(str.begin(), str.end());
    return str;
}

int main() {
    string str = "Hello";
    cout << "Reversed string: " << reverseString(str);
    return 0;
}
