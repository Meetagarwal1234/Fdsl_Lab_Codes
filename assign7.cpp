#include<iostream>
using namespace std;
class node{
    public:
    string nm;
    string post;
    int prn;
    node* next;
};
void display(node*&head,node*&tail){
    node *trav=head;
    cout<<"\nPost\tName\tPrn\n";
    while(trav!=tail){
        cout<<trav->post<<"\t"<<trav->nm<<"\t"<<trav->prn<<"\n";
        trav=trav->next;
    }
}
void insertmembers(node* &head,node* &tail){
    node *temp=new node();
    cout<<"Enter the name of the member :";
    cin>>temp->nm;
    cout<<"Enter the prn of the member :";
    cin>>temp->prn;
    temp->post="Member";
    temp->next=head->next;
    head->next=temp;
}

void removepresident(node* &head){
    node *temp=head;
    head=head->next;
    temp->next=NULL;
    delete temp;
    head->post="President";
}

void removesecretary(node* &head,node*&tail){
    node *prev=head;
    node *curr=head;
    curr=curr->next;
    while(curr->next!=NULL){
        curr=curr->next;
        prev=prev->next;
    }
    prev->next=NULL;
    prev->post="Secretary";
    delete curr;
}

void removemember(node* &head,node*&tail,int pos){
    node *prev=head;
    node *curr=head;
    curr=curr->next;
    for(int i=1;i<pos-1;i++){
        curr=curr->next;
        prev=prev->next;
    }
    prev->next=curr->next;
    curr->next=NULL;
    delete curr;
}

void createpressec(node*&head,node*&tail){
    cout<<"Enter the name of the president :";
    node *temp=new node();
    cin>>temp->nm;
    cout<<"Enter the prn of the president :";
    cin>>temp->prn;
    temp->post="President";
    head=temp;
    cout<<"Enter the name of the secretary :";
    node *temp1=new node();
    cin>>temp1->nm;
    cout<<"Enter the prn of the secretary :";
    cin>>temp1->prn;
    temp1->post="Secretary";
    head->next=temp1;
    temp1->next=NULL;
}
int main(){
    node* head=NULL;
    node* tail=NULL;
    createpressec(head,tail);
    //display(head,tail);
    int s;
    do{
        cout<<"\n**Menu***\n";
        cout<<"1.Enter details of members\n";
        cout<<"2.Display data\n";
        cout<<"3.Remove president\n";
        cout<<"4.Remove secretary\n";
        cout<<"5.Remove member\n";
        cout<<"6.Break\n";
        cout<<"Enter your choice :\n";
        cin>>s;
        switch(s){
            case 1:
            int n;
            cout<<"Enter the number of members\n";
            cin>>n;
            for(int i=0;i<n;i++){
                insertmembers(head,tail);
            }
            break;
            case 2:
            display(head,tail);
            break;
            case 3:
            removepresident(head);
            display(head,tail);
            break;
            case 4:
            removesecretary(head,tail);
            display(head,tail);
            break;
            case 5:
            cout<<"Enter your position :";
            int pos;
            cin>>pos;
            removemember(head,tail,pos);
            display(head,tail);
            break;
        }
    }while(s!=6);
}
//12
// 
//4 10 11
//8 13 