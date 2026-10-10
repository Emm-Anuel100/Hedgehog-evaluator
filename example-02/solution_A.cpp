#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    // O(1) mathematical solution
    std::cout << (n * (n + 1)) / 2 << std::endl;
    return 0;
}
