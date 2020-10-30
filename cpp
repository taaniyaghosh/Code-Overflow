#include<bits/stdc++.h>
#define int long long int
using namespace std;
int32_t main()
{
	int t;
	cin>>t;
	while(t--)
	{
	
  int h,p;
  cin>>h>>p;
  int a=h, b=p;
  while(a>0 && b>0)
  {
  	a=a-b;
  	b=b/2;
  }
  if(a<=0)
  {
  	cout<<"1"<<endl;
  }else
  {
  	cout<<"0"<<endl;
  }
}
	}
