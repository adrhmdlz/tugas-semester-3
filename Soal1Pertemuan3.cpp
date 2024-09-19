#include<iostream>
#include<cstdlib>

using namespace std;

// Fungsi untuk menghitung luas persegi
float luasPersegiPanjang(int panjang, int lebar) {
  return panjang * lebar;
};

int main(int argc, char* argv[]) {
  if (argc != 3) {
    cout << "Input tidak valid" << endl;
    return 1;
  }

  // Input 1 = panjang, input 2 = lebar
  int panjang = atoi(argv[1]);
  int lebar = atoi(argv[2]);

  cout << "Luas Persegi Panjang adalah: " << luasPersegiPanjang(panjang, lebar) << endl;

  return 0;
}
