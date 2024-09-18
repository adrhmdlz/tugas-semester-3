#include<iostream>

using namespace std;

int main() {
  int array[2][2][2];

  cout << "Masukan angka ke dalam array 3 dimensi:" << endl;
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
      for (int k = 0; k < 2; k++) {
        cout << "Angka pada lapisan ke-" << i + 1 << ", baris ke-" << j + 1 << ", kolom ke-" << k + 1 << ": ";
        cin >> array[i][j][k];
      }
    }
    cout << endl;
  }

  cout << "\nArray 3 dimensi yang dimasukan: " << endl;
  for (int i = 0; i < 2; i++) {
    cout << "Angka di lapisan ke-" << i + 1 << ": " << endl;
    for (int j = 0; j < 2; j++) {
      for (int k = 0; k < 2; k++) {
        cout << array[i][j][k] << " ";
      }
      cout << endl;
    }
    cout << endl;
  }
}