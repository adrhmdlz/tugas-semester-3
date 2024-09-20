#include<iostream>
#include<string>

using namespace std;

struct Mahasiswa {
  string nim;
  string nama[30];
  struct Nilai {
    // Misal 5 mata kuliah
    float ujian[5];
    float tugas[5];
  } nilai;
};

float rataRataNilai(float nilai[5], float jumlahMatkul) {
  int sum = 0;

  for (int i = 0; i < 5; i++) {
    sum += nilai[i];
  }

  return sum / jumlahMatkul;
}

int main() {
  Mahasiswa mahasiswa1;

  cout << "Masukan Nama Mahasiswa: ";
  std::getline(cin, mahasiswa1.nama);
  cout << "Masukan NIM Mahasiswa: ";
  cin >> mahasiswa1.nim;
  cout << "Masukan Nilai Ujian:" << endl;
  for (int i = 0; i < 5; i++) {
    cout << "Mata Kuliah ke-" << i + 1 << ": ";
    cin >> mahasiswa1.nilai.ujian[i];
  }
  cout << "Masukan Nilai Tugas: " << endl;
  for (int i = 0; i < 5; i++) {
    cout << "Mata Kuliah ke-" << i + 1 << ": ";
    cin >> mahasiswa1.nilai.tugas[i];
  }

  cout << "\nData Mahasiswa" << endl;
  cout << "Nama: " << mahasiswa1.nama << endl;
  cout << "NIM: " << mahasiswa1.nim << endl;
  cout << "Rata-rata Nilai Ujian: " << rataRataNilai(mahasiswa1.nilai.ujian, 5.0) << endl;
  cout << "Rata-rata Nilai Tugas: " << rataRataNilai(mahasiswa1.nilai.tugas, 5.0) << endl;
}