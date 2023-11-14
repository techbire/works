#include<iostream>
using namespace std;
int main(){
 cout<<"ENTER YOUR COST PRICE:";
 int cp;
 cin>>cp;
 cout<<"ENTER YOUR SELLING PRICE:";
 int sp;
 cin>>sp;
 if(sp>cp){ 
    cout<<"PROFIT";
 }
 if(sp<cp){
 cout<<"LOSS";

 }
}