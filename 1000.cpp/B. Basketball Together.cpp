#include <bits/stdc++.h>
using namespace std;

int main() {
    int t = 1;

    while (t--) {
        long long N, D; cin >> N >> D;
        vector<long long> p;
        for (int i = 0; i < N; ++i) {
            long long ele; cin >> ele;
            p.push_back(ele);
        }
        int ans = 0;
        sort(p.begin(), p.end(), greater<int>());
        int j = N - 1;
        for (int i = 0; i < N; ++i) {
            long req_ppl = D / p[i] + 1;
            if (j - i + 1 < req_ppl) break;
            j -= (req_ppl - 1);
            ans += 1;
        }
        cout << ans << endl;
    }

}