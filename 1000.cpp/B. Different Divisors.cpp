#include <bits/stdc++.h>
using namespace std;

bool isprime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 or n % 3 == 0) return false;

    int limit = (int)sqrt(n);
    for (int i = 5; i <= limit; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

void solve(){
    int d; cin >> d;

    int first_bound = 1 + d;
    while (isprime(first_bound) == false) first_bound++;

    int second_bound = first_bound + d;
    while (isprime(second_bound) == false) second_bound++;

    cout << first_bound * second_bound << endl;

}


int main(){
    int t; cin >> t;
    while (t--) {
        solve();
    }
}