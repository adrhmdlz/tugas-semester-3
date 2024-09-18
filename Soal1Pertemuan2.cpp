#include<iostream>
#include<iomanip>

using namespace std;

int main() {
  // mendefinisikan string
  char kalimat[] = {"Jl. Candi Mulyo 1 No. 25"};
  char *pKarakter; // pointer ke char
  int lowerCase = 0; // penghitung huruf kecil
  int upperCase = 0; // penghitung huruf besar
  int number = 0; // penghitung angka
  int otherChar = 0; // penghitung karakter lainnya
  pKarakter = kalimat;

  while(*pKarakter) {
    char kar = *pKarakter;

    if (kar >= 'a' && kar <= 'z') {
      lowerCase++;
    } else if (kar >= 'A' && kar <= 'Z') {
      upperCase++;
    } else if (kar >= '0' && kar <= '9') {
      number++;
    } else {
      otherChar++;
    }
    pKarakter++;
  }

  cout << "Jumlah huruf kecil: " << lowerCase << endl;
  cout << "Jumlah huruf besar: " << upperCase << endl;
  cout << "Jumlah Angka: " << number << endl;
  cout << "Jumlah Lainnya: " << otherChar << endl;
  cout << "Total Huruf: " << (lowerCase + upperCase + number + otherChar) << endl;
}