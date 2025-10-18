#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    long long min_of_all_arr = INT_MAX, sum = 0;
    vector<long> second_min;
    while (n--) {
        long long k;
        cin >> k;
        vector <long long> arr;
        while(k--) {
            long long m;
            cin >> m;
            arr.push_back(m);
        }
        sort(arr.begin(), arr.end());
        if (min_of_all_arr > arr[0]) min_of_all_arr = arr[0];
        second_min.push_back(arr[1]);
        sum += arr[1];
    }
    long long ans = sum - *min_element(second_min.begin(), second_min.end()) + min_of_all_arr;
    cout << ans << endl;
}

int main() {
    int n;
    cin >> n;
    while (n--){
        solve();
    }
}