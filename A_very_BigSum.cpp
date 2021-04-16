#include <iostream>
using namespace std;
 int main()
{
long int i,n,sum=0,a[200000];
cin>>n;
for(i=0;i<n;i++)
{
    cin>>a[i];
}
for(i=0;i<n;i++)
{
    sum=sum+a[i];
}
cout<<sum;
}
