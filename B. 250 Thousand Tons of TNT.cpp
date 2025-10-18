#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve() {
    int n; cin >> n;
    int a[n];
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    ll ans = 0;
    for (int num = 1; num < n; ++num) {
        if (n % num == 0) { // num is a factor of n
            ll mini = 1e18, maxi = -1e18;
            for (int i = 0; i < n; i += num) {
                ll sum = 0;
                for (int j = i; j < i + num; ++j) {
                    sum += a[j];
                }
                maxi = max(maxi, sum);
                mini = min(mini, sum); 
            }
            ans = max(ans, maxi - mini);
        }
    }
    cout << ans << endl;
}

int main() {
    int t; cin >> t;
    while (t--) {
        solve();
    }
}