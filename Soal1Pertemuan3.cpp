#include<iostream>

using namespace std;

float hitungLuasPersegi(int panjang, int lebar);

int main() {
  int p, l;

  cout << "Masukan nilai panjang: ";
  cin >> p;

  cout << "Masukan nilai lebar: ";
  cin >> l;

  cout << "Luas persegi adalah: " << hitungLuasPersegi(p, l) << endl;
}

float hitungLuasPersegi(int panjang, int lebar) {
  return panjang * lebar;
}