#include<bits/stdc++.h>
using namespace std;
int front=0,rear=0;
#define N 20
string arr[N];

void display(){
    if(front==rear)cout<<"Queue is empty";
    cout<<"\nYour current queue :\n";
    for(int i=front;i<rear;i++){
        cout<<arr[i]<<" ";
    }
}

void push(int count){
    if(rear==N){
        cout<<"Queue is full";
        return;
    }
    cout<<"Enter your element :";
    string str="Job"+to_string(count);
    arr[rear]=str;
    rear++;
    display();

}

void pop(){
    if(front==rear){
        cout<<"Your queue is empty";
        return;
    }
    arr[front]=-1;
    front++;
    if(front==rear){
        front=0;
        rear=0;
    }
    display();
}

void qfront(){
    if(front==rear){
        cout<<"Queue is empty";
    }
    cout<<arr[front];
}

int main(){
    int count=1;
    int s;
    do{
        cout<<"\n**Menu**\n";
        cout<<"1.Push()\n";
        cout<<"2.Pop()\n";
        cout<<"3.Front()\n";
        cout<<"4.Display()\n";
        cout<<"5.Break\n";
        cout<<"Enter your choice :";
        cin>>s;
        switch(s){
            case 1:
            push(count);
            count++;
            break;
            case 2:
            pop();
            break;
            case 3:
            qfront();
            break;
            case 4:
            display();
            break;
            case 5:
            break;
        }
    }while(s!=5);
}