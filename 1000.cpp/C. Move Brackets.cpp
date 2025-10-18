#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;
    string s; cin >> s;

    int cnt = 0;
    int ans = 0;
    for (auto chr : s) {
        if (chr == ')') cnt -= 1;
        else cnt += 1;

        ans = max(ans, -cnt);
    }
    
    cout << ans << endl;

}

int main() {
    int t; cin >> t;
    while(t--) {
        solve();
    }
}