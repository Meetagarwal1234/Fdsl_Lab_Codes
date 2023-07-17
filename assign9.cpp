#include<bits/stdc++.h>
using namespace std;
int main(){
    stack<char> st;
    cout<<"Enter your string :";
    string s;
    getline(cin,s);
    for(int i=0;i<s.length();i++){
        st.push(s[i]);
    }
    string ans="";
    while(!st.empty()){
        char c=st.top();
        st.pop();
        ans+=c;
    }
    cout<<"Reversed string :"<<ans;
    if(s==ans){
        cout<<"\nYour string is pallindrome";
    }
    else{
        cout<<"\nString is not pallindrome";
    }
}