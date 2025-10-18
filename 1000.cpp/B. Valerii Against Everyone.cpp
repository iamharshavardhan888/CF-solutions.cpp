#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;
    unordered_set<int> s;
    for (int i = 0; i < n; ++i) {
        int ele; cin >> ele;
        s.insert(ele);
    }
    cout << (s.size() < n ? "YES" : "NO") << endl;
}

int main() {
    int t; cin >> t;
    while (t--) {
        solve();
    }
}