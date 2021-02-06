#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    int k = n-1;
    for(int i=1;i<=n;i++){
        for(int j=0;j<k;j++)
        {
            cout<<" ";
        }
        k = k -1;
        for(int j=i;j<2*i;j++){
            cout<<j;
        }
        cout<<endl;
    }
    return 0;
}
