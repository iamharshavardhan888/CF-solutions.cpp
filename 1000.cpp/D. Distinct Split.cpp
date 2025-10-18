#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;

        vector<int> pre, suf;
        pre.push_back(0);
        suf.push_back(0);

        unordered_map<char, int> freq1, freq2;

        for (int i = 0; i < n; i++) {
            if (freq1.find(s[i]) == freq1.end()) {
                pre.push_back(pre.back() + 1);
                freq1[s[i]] = 1;
            } else {
                pre.push_back(pre.back());
            }

            int j = n - 1 - i;
            if (freq2.find(s[j]) == freq2.end()) {
                suf.push_back(suf.back() + 1);
                freq2[s[j]] = 1;
            } else {
                suf.push_back(suf.back());
            }
        }

        pre.erase(pre.begin()); 
        suf.erase(suf.begin()); 
        reverse(suf.begin(), suf.end());

        int ans = 0;
        for (int i = 0; i < n - 1; i++) {
            ans = max(ans, pre[i] + suf[i + 1]);
        }

        cout << ans << "\n";
    }
    return 0;
}
