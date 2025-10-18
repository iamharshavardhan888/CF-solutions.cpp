#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m; cin >> n >> m;
    int min_ele = INT_MAX, sum = 0;
    int cnt = 0; // Negative count
    for (int i = 0; i < n * m; ++i) {
        int ele; cin >> ele;
        min_ele = min(min_ele, abs(ele));
        cnt += ((ele < 0) ? 1 : 0);
        sum += abs(ele);
    }
    if (cnt % 2) cout << sum - 2 * min_ele << endl;
    else cout << sum << endl;

}


int main() {
    int t; cin >> t;
    while(t--){
        solve();
    }
}