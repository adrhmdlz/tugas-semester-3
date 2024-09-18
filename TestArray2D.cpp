#include<iostream>

using namespace std;

int main() {
  int array[3][3];

  cout << "Masukan angka ke dalam matriks (3x3): " << endl;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cout << "Angka pada baris ke-" << i + 1 << ", kolom ke-" << j + 1 << ": ";
      cin >> array[i][j];
    }
  }

  cout << "\nMatriks yang terbentuk adalah:" << endl;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cout << array[i][j] << " ";
    }
    cout << endl;
  }
}