#include<iostream>
#define MAX 100

using namespace std;

int stack[MAX];
int top = -1;

void push(int item) {
  if (top >= MAX - 1) {
    cout << "Stack Penuh" << endl;
    return;
  }
  stack[++top] = item;
}

int pop() {
  if (top < 0) {
    cout << "Stack Kosong" << endl;
    return -1;
  }
  return stack[top--];
}

int peek() {
  if (top < 0) {
    return -1;
  }

  return stack[top];
}

void display() {
  cout << "Stack: ";
  for (int i = 0; i <= top; i++) {
    cout << stack[i] << " ";
  }
  cout << endl;
}

int main() {
  int input;

  do {
    cout << "1. Push" << endl;
    cout << "2. Pop" << endl;
    cout << "3. Peek" << endl;
    cout << "4. Display" << endl;
    cout << "5. Exit" << endl;
    cout << "Masukkan pilihan: ";
    cin >> input;
    if (input == 1) {
      int input;
      cout << "Push Element: ";
      cin >> input;
      push(input);
    } else if (input == 2) {
      pop();
    } else if (input == 3) {
      cout << "Indeks teratas: " << peek() << endl;
    } else if (input == 4) {
      display();
    }
  } while (input != 5);
}