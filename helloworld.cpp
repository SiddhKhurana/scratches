#include <iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        string x = "";
        for(int j=i;j<=2*i;j++){
            x += (string)j;
        }
        cout<<x<<endl;
    }
    return 0;
}