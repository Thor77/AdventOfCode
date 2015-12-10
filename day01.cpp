#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  bool part2 = false;
  string data;
  ifstream infile("input/01");
  infile >> data;
  infile.close();
  int counter = 0;
  for (int i = 0; i < data.size(); i++) {
    char c = data[i];
    if (data[i] == '(') {
      counter++;
    } else {
      counter--;
    }
    if (counter == -1 && part2) {
      cout << "Reached basement (floor = -1) " << i + 1 << endl;
      break;
    }
  }
  cout << counter << endl;
}
