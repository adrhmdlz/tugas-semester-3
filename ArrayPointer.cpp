#include<iostream>

using namespace std;

int main() {
  char hobi[4][10] = {"renang", "basket", "lukis", "musik"};
  char *hobiPtr[4];

  for (int i = 0; i < 4; i++) {
    hobiPtr[i] = hobi[i];
  }

  for (int i = 0; i < 4; i++) {
    cout << hobiPtr[i] << endl;
  }
}