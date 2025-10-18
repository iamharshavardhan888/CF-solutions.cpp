#include <bits/stdc++.h>
using namespace std;

vector<int> intersection_region(int a, int b, int c, int d) {
    if (a < c) a = c;
    if (b > d) b = d;
    return {a, b};
}

int main() {
    int t; cin >> t;
    while(t--) {
        int n, x; cin >> n >> x;
        vector<int> v;
        for (int i = 0; i < n; ++i) {
            int ele; cin >> ele;
            v.push_back((int)ele);
        }
        int l = v[0] - x, r = v[0] + x;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            vector<int> v0 = intersection_region(l, r, v[i] - x, v[i] + x);
            l = v0[0];
            r = v0[1];
            if (l > r) {
                ans++;
                l = v[i] - x;
                r = v[i] + x;
            }
        }
        cout << ans << endl;
    }
}