#include<iostream>
#include<cstring>

using namespace std;

int main() {
  char kalimat[] = "Jl. Candi Mulyo 1 No. 25";
  char *pKarater = kalimat;

  cout << "Kalimat awal: " << kalimat << endl;

  int posisiAwal;
  cout << "Masukan posisi awal karakter: ";
  cin >> posisiAwal;

  int posisiAkhir;
  cout << "Masukan posisi akhir karakter: ";
  cin >> posisiAkhir;

  // validasi posisi
  if (posisiAwal < 0 || posisiAkhir >= strlen(kalimat) || posisiAwal > posisiAkhir) {
    cout << "Posisi tidak valid" << endl;
    return 1;
  }

  for (int i = posisiAwal; i <= posisiAkhir; i++) {
    *(pKarater + i) = 'X';
  }

  cout << "Kalimat setelah dirubah: " << pKarater << endl;
}