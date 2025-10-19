#include <bits/stdc++.h>
using namespace std;

// Function to compute difference between max and min digit of number
int res(int k) {
    string s = to_string(k); // not 'a'
    char max_digit = *max_element(s.begin(), s.end());
    char min_digit = *min_element(s.begin(), s.end());
    return max_digit - min_digit; // char subtraction gives correct int difference
}

void solve() {
    int a, b;
    cin >> a >> b;

    int ans = 0;
    int num = a;

    for (int i = a; i <= b; i++) {
        int val = res(i);
        if (val == 9) {
            cout << i << endl;
            return;
        }

        if (val > ans) {
            ans = val;
            num = i;
        }
    }

    cout << num << endl; // fixed typo 'end' -> 'endl'
}

int main() {
    int n;
    cin >> n;
    while (n--) {
        solve();
    }
    return 0;
}
