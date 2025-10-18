#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        long long a, b;
        cin >> a >> b;
        long long ans = LLONG_MAX;
        for (long long addition = 0; addition < 32; addition++) {
            long long operations = addition;
            long long new_b = b + addition;
            if (new_b == 1)
                continue;
            long long copy_a = a;
            while (copy_a > 0) {
                copy_a /= new_b;
                operations++;
            }
            ans = min(ans, operations);
        }
        cout << ans << "\n";
    }
    return 0;
}
