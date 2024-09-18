#include<iostream>

using namespace std;

int main() {
  int array[5];

  cout << "Masukan 5 angka ke dalam array: " << endl;
  for (int i = 0; i < 5; i++) {
    cout << "Array ke-" << i + 1 << ": ";
    cin >> array[i];
  }

  cout << "\nAngka yang dimasukan ke array: " << endl;
  for (int i = 0; i < 5; i++) {
    cout << "Array ke-" << i + 1 << ": " << array[i] << endl;
  }

  return 0;
}