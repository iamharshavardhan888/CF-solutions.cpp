#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll calDist(pair<int, int> a, pair<int, int> b) {
    ll dx = (ll)a.first - (ll)b.first;
    ll dy = (ll)a.second - (ll)b.second;
    return llabs(dx) + llabs(dy);
}

void solve() {
    int n, k, a, b; cin >> n >> k >> a >> b;
    vector<pair<int, int>> v(n);
    for (int i = 0; i < n; ++i) cin >> v[i].first >> v[i].second;

    if (k == 0) {
        cout << calDist(v[a - 1], v[b - 1]) << endl;
        return;
    }

    ll d1 = LLONG_MAX, d2 = LLONG_MAX;
    for (int i = 0; i < k; ++i) {
        d1 = min(calDist(v[i], v[a - 1]), d1);
        d2 = min(calDist(v[i], v[b - 1]), d2);
    }

    cout << min(d1 + d2, calDist(v[a - 1], v[b - 1])) << endl; 
}

int main() {
    int t; cin >> t;
    while (t--) solve();
}