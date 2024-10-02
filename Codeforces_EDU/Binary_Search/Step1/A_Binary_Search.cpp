#include <bits/stdc++.h>
using namespace std;


bool isAvail(vector <int> &v, int key){
    bool found = false;
    int n = v.size();
    int k = 0;
    int hi = n-1;
    int low = 0;
    while(hi >= low){
        k = (hi+low)/2;
        if(v[k]<key){
            low = k+1;
        }
        else if(v[k]>key){
            hi = k-1;
        }
        else{
            found = true;
            break;
        }
    }
    return found;
}

void printsoln(vector <int> &v1, vector <int> &v2,int n1, int n2 ){
    for (int i = 0;i<n2;i++){
        bool found = isAvail(v1,v2[i]);
        if(found) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
}


int main(){
    int n1,n2;
    cin>>n1>>n2;
    vector <int> v1(n1);
    for(int i=0;i<n1;i++){
        cin>>v1[i];
    }

    vector <int> v2(n2);
    for(int i=0;i<n2;i++){
        cin>>v2[i];
    }

    printsoln(v1,v2,n1,n2);
    return 0;
}