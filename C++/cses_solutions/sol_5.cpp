#include <iostream>
using namespace std;
int main() {
  long long unsigned int n;
  cin >> n;
  if(n == 3 || n == 2) {
    cout << "NO SOLUTION";
    return 0;
  }
  for(int i = 2; i <= n ; i+=2) {
    cout << i << " ";
  }
  for(int i = 1; i <= n ; i+=2) {
    cout << i << " ";
  }
}