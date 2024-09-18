#include<iostream>

using namespace std;

struct mahasiswa {
  string nama;
  string nim;
  string kelas;
  int no_absen;
};

int main() {
  mahasiswa mahasiswa1;

  cout << "Masukan data Mahasiswa:" << endl;
  cout << "Nama Mahasiswa: ";
  cin >> mahasiswa1.nama;
  cout << "Nomor NIM: ";
  cin >> mahasiswa1.nim;
  cout << "Kelas: ";
  cin >> mahasiswa1.kelas;
  cout << "No. Absen Mahasiswa: ";
  cin >> mahasiswa1.no_absen;

  cout << "\nInformasi Mahasiswa:" << endl;
  cout << "Nama: " << mahasiswa1.nama << endl;
  cout << "NIM: " << mahasiswa1.nim << endl;
  cout << "Kelas: " << mahasiswa1.kelas << endl;
  cout << "No. Absen: " << mahasiswa1.no_absen << endl;
}