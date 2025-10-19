#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll calwater(vector<int>& a, int h, int n) {
    ll ans = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] < h) ans += (h - a[i]);
    }
    return ans;
}

void solve() {
    int n, x; cin >> n >> x;
    vector<int> a(n);
    int maxi = INT_MIN;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        maxi = max(maxi, a[i]);
    }
    ll l = 0, r = x + maxi, cnt = 0;
    while (l < r) {
        ll mid = (l + r + 1) / 2;
        ll capacity = calwater(a, mid, n);
        if (capacity <= x) {
            l = mid;
        }else r = mid - 1;
    }
    cout << l << endl;
}

int main() {
    int t; cin >> t;
    while (t--) solve();
}