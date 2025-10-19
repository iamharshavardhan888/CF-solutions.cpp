#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, x; cin >> n >> x;
    int val = 0;
    for (int i = 0; i < 3; ++i) {
        int flag = 1;
        for (int j = 0; j < n; ++j) {
            int k; cin >> k;
            if ((k | x) != x) flag = 0;
            if (flag) val |= k;
        }
    }
    
    if (val == x) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main() {
    int t; cin >> t;
    while (t--) solve();
}
