#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std; 
int binarySearch(int arr[], int l, int r, int x) 
{ 
    if (r>=l) 
    { 
        int mid = l + (r - l)/2; 
        if (arr[mid] == x) 
            return mid; 
        if (arr[mid] > x) 
            return binarySearch(arr, l, mid-1, x); 
        return binarySearch(arr, mid+1, r, x); 
    } 
    return -1; 
} 
int findPos(int arr[], int key) 
{ 
    int l = 0, h = 1; 
    int val = arr[0]; 
  
    // Find h to do binary search 
    while (val < key) 
    { 
        l = h;        // store previous high 
        h = 2*h;      // double high index 
        val = arr[h]; // update new val 
    } 
    return binarySearch(arr, l, h, key); 
} 
int IndexOf(int arr[],int key,int i, int N){
    for(; i<N ; i++) {
        if(arr[i] ==  key){
            break;
        }
    }
    return i;
}
 
int main()
{
    int j;
    cin >> j;
    for(int z=0; z<j; z++)
    {
        int N,K,i1,i2,i3;
        int P[N],arr[N];
        cin >>N>>K;
        for(int i=0; i<N; i++)
        {
            cin >> P[i];
            arr[i] = P[i];
        }
        sort(arr, arr+N);
        int count = 0;
        int flag = 1;
        int temp;
        vector<int> ans;
        for(int i = 0; i <N-3; i++)
        {
            i3 = IndexOf(P,arr[i],i,N);
            i1 = i;
            i2 = findPos(arr,P[i]);
            if(i1 == i2)
            {
                continue;
                
            }
            else if(i2 == i3)
            {
                i2 = i1+1;
            }
            if(i2 == i3)
            {
                if(i3 == N-1)
                {
                    flag = 0;
                    break;
                }
                i2 = i3+1;
            }
            temp = P[i1];
            P[i1] = P[i3];
            P[i3] = P[i2];
            P[i2] = temp;
            ans.push_back(i1);
            ans.push_back(i2);
            ans.push_back(i3);
            count++;
        }
        if(flag ==1)
        {
            cout << count <<"\n";
            for (auto i = ans.begin(); i != ans.end(); i = i+3) 
                cout << *i+1<<" "<<*(i+1)+1<<" "<<*(i+2)+1<<"\n";
        }
        else
        {
            cout << "-1"<<"\n";
        }
    }
	// your code goes here
	return 0;
}
