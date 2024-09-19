#include<iostream>

using namespace std;

// Fungsi menghitung rata-rata
float rataRata(float totalNilai, float jumlahPelajaran) {
  return totalNilai / jumlahPelajaran;
}

int main() {
  int jumlahSiswa;

  // Input jumlah siswa
  cout << "Masukan jumlah siswa: ";
  cin >> jumlahSiswa;

  // Pengalokasian memori secara dinamis tergantung berapa banyaknya 
  // siswa yang akan diinput
  float** nilai = new float*[jumlahSiswa];
  for (int i = 0; i < jumlahSiswa; i++) {
    nilai[i] = new float[3];
  }

  cin.ignore();

  // Masukan nilai satu-persatu
  for (int i = 0; i < jumlahSiswa; i++) {
    cout << "Masukan nilai untuk siswa ke-" << i + 1 << endl;
    cout << "Bahasa Indonesia: ";
    cin >> nilai[i][0];
    cout << "Bahasa Inggris: ";
    cin >> nilai[i][1];
    cout << "Matematika: ";
    cin >> nilai[i][2];
    cout << endl;
  }

  // Tampilkan semua nilai yang dimasukan
  cout << "Nilai masing-masing siswa:" << endl;
  for (int i = 0; i < jumlahSiswa; i++) {
    float totalNilai = 0;
    for (int j = 0; j < 3; j++) {
      totalNilai += nilai[i][j];
    }
    cout << "Nilai siswa ke-" << i + 1 << endl;
    cout << "Bahasa Indonesia: " << nilai[i][0] << endl; 
    cout << "Bahasa Inggris: " << nilai[i][1] << endl; 
    cout << "Matematika: " << nilai[i][2] << endl; 
    cout << "Rata-rata: " << rataRata(totalNilai,  3.0) << endl;
    cout << endl;
  }

  // Dealokasi memori
  for (int i = 0; i < jumlahSiswa; i++) {
    delete[] nilai[i];
  }
  delete[] nilai;
}