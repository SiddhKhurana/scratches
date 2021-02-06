#include <iostream>
using namespace std;

int main(){
    int basic;                    // find the salary
    char grade;
    cin>>basic;
    cin>>grade;
    int allow;
    if(grade =='A'){
        allow=1700;
    }
    else if(grade=='B'){
        allow=1500;
    }
    else{
        allow = 1300;
    }
    cout<<basic*1.59+allow<<endl;
    return 0;
}

int main(){                      // Find the power
    int x,n;
    cout<<"Enter Base";
    cin>>x;
    cout<<"Enter Power";
    cin>>n;
    int temp;
    temp=x;
    if(x==0 && n==0)
    {
        cout<<1<<endl;
    }                           
    else{
        while(n>1){
            x*=temp;
            n--;
        }
        cout<<x;
    }
    
}


int main()                                 // sum of odd and even digits
{    int y;
    cout<<"Enter the number: ";
    cin>>y;
    int sum_odd=0;
    int sum_even=0;
    for(int n=y;n>0;n=n/10)
    {
        int rem = n%10;
        if (rem%2==0)
        {
            sum_even+=rem;
        }
        else
        {
            sum_odd+=rem;
        }
    }
    cout<<sum_even<<' '<<sum_odd<<endl;  
    return 0;    
}
