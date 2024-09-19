#include<iostream>

using namespace std;

int main() {
  int jumlahOrang;

  // Input jumlah orang
  cout << "Masukan jumlah orang yang akan diinput: ";
  cin >> jumlahOrang;

  // Pengalokasian memori secara dinamis tergantung berapa banyaknya 
  // orang yang akan diinput
  char** nama = new char*[jumlahOrang];
  for (int i = 0; i < jumlahOrang; i++) {
    nama[i] = new char[31];
  }

  cin.ignore();

  // Masukan nama satu-persatu
  for (int i = 0; i < jumlahOrang; i++) {
    cout << "Masukan nama orang ke-" << i + 1 << ": ";
    cin.getline(nama[i], 31);
  }

  // Tampilkan semua nama yang dimasukan
  cout << "\nData nama orang yang terinput:" << endl;
  for (int i = 0; i < jumlahOrang; i++) {
    cout << i + 1 << ". " << nama[i] << endl;
  }

  // Dealokasi memori
  for (int i = 0; i < jumlahOrang; i++) {
    delete[] nama[i];
  }
  delete[] nama;

  return 0;
}