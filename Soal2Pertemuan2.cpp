#include<iostream>

using namespace std;

int main() {
  char kalimat[] = "Jl. Candi Mulyo 1 No. 25";
  char *pKarakter;
  char karakterDicari;
  bool karakterDitemukan = false;
  int posisiKarakter = 0;
  pKarakter = kalimat;

  cout << "Masukan karakter yang ingin dicari: ";
  cin >> karakterDicari;

  while (*pKarakter) {
    if (*pKarakter == karakterDicari) {
      karakterDitemukan = true;
      cout << "Huruf yang dicari ada di posisi " << posisiKarakter << endl;
      break;
    }

    pKarakter++;
    posisiKarakter++;
  }

  if (!karakterDitemukan) {
    cout << "Huruf tidak ada di kalimat" << endl;
  }

  return 0;
}