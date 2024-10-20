#include<iostream>
#define MAX 10

using namespace std;

int stack[MAX];
int top1 = -1;
int top2 = MAX;

void push1(int item) {
  if (top1 + 1 == top2) {
    cout << "Stack 1 overflow!" << endl;
    return;
  }

  stack[++top1] = item;
}

void push2(int item) {
  if (top2 - 1 == top1) {
    cout << "Stack 2 overflow!" << endl;
    return;
  }

  stack[--top2] = item;
}

int pop1() {
  if (top1 < 0) {
    cout << "Stack 1 underflow!" << endl;
    return -1;
  }

  return stack[top1--];
}

int pop2() {
  if (top2 >= MAX) {
    cout << "Stack 2 underflow!" << endl;
    return -1;
  }

  return stack[top2++];
}

int peek1() {
  if (top1 < 0) {
    return -1;
  }

  return stack[top1];
}

int peek2() {
  if (top1 >= MAX) {
    return -1;
  }

  return stack[top2];
}

int main() {
  push1(10);
  push1(20);
  pop1();
  push2(25);
  push2(15);
  cout << peek1() << endl;
  cout << peek2() << endl;
}