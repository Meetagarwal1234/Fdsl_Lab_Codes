#include<iostream>
using namespace std;
int front=-1,rear=-1;
#define N 7
int arr[N];
void display(){
    if(front==-1){
        cout<<"Deque is empty ";
        return;
    }
    if(rear>=front){
        for(int i=front;i<=rear;i++){
            cout<<arr[i]<<" ";
        }
    }
    else{
        for(int i=front;i<N;i++){
            cout<<arr[i]<<" ";
        }
        for(int i=0;i<=rear;i++){
            cout<<arr[i]<<" ";
        }
    }
}
void push(){
    if((front==0 && rear==N-1) || rear==(front-1)%(N-1)){
        cout<<"Deque is full";
        return;
    }
    cout<<"Enter the element :";
    int n;
    cin>>n;
    if(front==0){
        front=N-1;
    }
    else if(front==-1){
        front=rear=0;
    }
    else{
        front--;
    }
    arr[front]=n;
}

void pop(){
    if(rear==-1){
        cout<<"Queue is empty";
        return;
    }
    if(rear==0){
        rear=N-1;
    }
    else if(front==rear){
        front=rear=-1;
    }
    else {
        rear--;
    }
}

int main(){
    int s;
    do{
        cout<<"\n**Menu**\n";
        cout<<"1.Push()\n";
        cout<<"2.Pop()\n";
        cout<<"3.Display()\n";
        cout<<"4.Break\n";
        cout<<"Enter your choice :";
        cin>>s;
        switch(s){
            case 1:
            push();
            display();
            break;
            case 2:
            pop();
            display();
            break;
            case 3:
            display();
            break;
            case 4:
            break;
        }
    }while(s!=4);
}