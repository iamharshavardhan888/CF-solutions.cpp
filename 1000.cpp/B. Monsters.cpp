#include <bits/stdc++.h>
using namespace std; 

void solve() {
    int n, k;
    cin >> n >> k;

    vector<pair<int,int>> v;
    for(int i = 0; i < n; ++i) {
        int ele;
        cin >> ele;
        if (ele % k == 0) {
            cout << i + 1 << " ";
        }else{
            v.push_back({ele % k, i + 1});
        } 
    }

    sort(v.begin(), v.end(), [](const pair<int,int> &a, const pair<int,int> &b) {
        if (a.first == b.first) {
            return a.second < b.second; 
        }
        return a.first > b.first; 
    });

    for(int i = 0; i < v.size(); ++i){
        cout << v[i].second << " ";
    }
    cout << endl;

}

int main() {
    int n;
    cin >> n;
    while (n--){
        solve();
    }
}