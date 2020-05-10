#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;
#define li(n) for(int i=0; i<n; i++)
#define lj(n) for(int j=0; j<n; j++)

class Totient {
public:
    int n;
    vector<int> phi;
    vector<int> primes;
    Totient(int n) {
        this->n = n;
        phi.resize(n+1, 0);
        li(n) phi[i+1] += i+1;
        for(int i=2; i <= n; i++) {
            if (phi[i] == i) {
                primes.push_back(i);
                for(int j = i; j <= n; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }
    }
};


int main() {
  return 0;
}
