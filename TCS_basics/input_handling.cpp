#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> parseInput(const string& input) {
    vector<int> result;
    stringstream ss(input);
    int num;
    char comma;

    while (ss >> num) {
        result.push_back(num);
        ss >> comma; // extract the comma
    }

    return result;
}



int main(){
    
    vector <int> v;
    string input;
    cin.clear();
    getline(cin,input);
    //cout<<input<<endl;

    v = parseInput(input);
    for(auto i:v){
        cout<<i<<" ";
    }   
    cout<<endl;

}