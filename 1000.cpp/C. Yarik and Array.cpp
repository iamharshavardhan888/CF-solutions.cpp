#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;
    vector<int> v(n);
    int _max = INT_MIN;
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
        _max = max(_max, v[i]);
    }
    if (_max < 0) {
        cout << _max << endl;
        return;
    }

    int sum = max(v[0], 0);
    int ans = sum;
    for (int i = 1; i < n; ++i) {
        if ((v[i] ^ v[i - 1]) & 1) {
            if (sum < 0) sum = v[i];
            else sum += v[i];
        }else sum = v[i];
        ans = max(ans, sum);
    }
    cout << ans << endl;

}

int main() {
    int t; cin >> t;
    while (t --) solve();
}