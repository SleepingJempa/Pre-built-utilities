#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;
#define li(n) for(int i=0; i<n; i++)
#define lj(n) for(int j=0; j<n; j++)

class DSU {

public:
    int size;
    int components;
    vector<int> component_size;
    vector<int> id;
    vector<int> degree;

    DSU(int size) {
        this->size = size;
        this->components = size;
        this->component_size.resize(size, 1);
        this->degree.resize(size, 0);
        this->id.resize(size);
        for(int i = 0; i < size; i++) {
            id[i] = i;
        }
    }

    int getSize() {
        return this->size;
    }

    int Find(int a) {
        int root = a;

        while(root != id[root]) {
            root = id[root];
        }

        while(a != root) {
            id[a] = root;
            a = id[a];
        }

        return root;
    }

    int Union(int a, int b) {
        int root_a = Find(a);
        int root_b = Find(b);

        if(root_a == root_b) {
            return root_a;
        } else {
            if (component_size[root_a] >= component_size[root_b]) {
                component_size[root_a] += component_size[id[root_b]];
                components--;
                return id[root_b] = root_a;
            } else {
                component_size[root_b] += component_size[id[root_a]];
                components--;
                return id[root_a] = root_b;
            }
        }
    }

    void Show() {
        for(int i=0; i<size; i++) {
            cout << i << ' ' << id[i] << endl;
        }
        cout << endl;
        for(int i=0; i<size; i++) {
            cout << i << ' ' << component_size[Find(i)] << endl;
        }
    }

};

int main() {
  return 0;
}
