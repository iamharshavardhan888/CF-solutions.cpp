#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve() {
    int n, q; cin >> n >> q;
    vector<int> a(n), b(q);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < q; ++j) cin >> b[j];

    int min = INT_MAX;
    for (int i = 0; i < q; ++i) {
        if (min > b[i]) {
            min = b[i];
            ll val = 1LL << min;
            for (int j = 0; j < n; ++j) {
                if (a[j] % val == 0) a[j] += (1LL << (min - 1));
            }
        }
    }
    for (int i = 0; i < n; ++i) cout << a[i] << " ";
    cout << endl;
}

int main() {
    int t; cin >> t;
    while (t--) solve();
}