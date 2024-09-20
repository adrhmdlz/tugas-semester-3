#include<iostream>

using namespace std;

void cekAngka(int angka[10], int *max, int *min) {
  *max = angka[0];
  *min = angka[0];

  for (int i = 1; i < 10; i++) {
    if (angka[i] > *max) {
      *max = angka[i];
    }
    if (angka[i] < *min) {
      *min = angka[i];
    }
  }
}

int main() {
  int angka[10];
  int max, min;

  cout << "Silahkan masukan 10 angka" << endl;
  for (int i = 0; i < 10; i++) {
    cout << "Masukan angka ke-" << i + 1 << ": ";
    cin >> angka[i];
  }

  cekAngka(angka, &max, &min);

  cout << "Hasil Pengecekan" << endl;
  cout << "Angka Terbesar: " << max << endl;
  cout << "Angka Terkecil: " << min << endl;
}