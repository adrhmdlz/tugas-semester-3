#include<iostream>
#include<cstdlib>

using namespace std;

int main(int argc, char* argv[]) {
  if (argc != 3) {
    cout << "Input tidak valid" << endl;
    return 1;
  }

  int m = atoi(argv[1]);
  int n = atoi(argv[2]);

  cout << "Tampilkan bilangan dari m(" << m << ") ke n(" << n << "): ";
  for (int i = m; i <= n; i++) {
    cout << i << " ";
  }
}