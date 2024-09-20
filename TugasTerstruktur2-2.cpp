#include<iostream>

using namespace std;

int main() {
  int array[2][5];

  for (int i = 0; i < 2; i++) {
    cout << "Masukan array ke-" << i + 1 << ": " << endl;
    for (int j = 0; j < 5; j++) {
      cout << "Element ke-" << i + 1 << ": ";
      cin >> array[i][j];
    }
  }

  int sum[5];
  for (int i = 0; i < 5; i++) {
    sum[i] = array[0][i] + array[1][i];
  }

  cout << "Hasil penjumlahan kedua array: ";
  for (int i = 0; i < 5; i++) {
    cout << sum[i] << " ";
  }
}