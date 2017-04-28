#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
  std::cout << "Enter the value N to produce:\n";
  int N;
  std::cin >> N;

  std::cout << "Enter the number of different denominations:\n";
  size_t denomCount;
  std::cin >> denomCount;

  std::vector<int> denominations(denomCount);
  for (size_t i = 0; i < denomCount; ++i) {
    std::cout << "Enter denomination #" << (i + 1) << ":\n";
    std::cin >> denominations[i];
  }

  // sort into descending order.
  std::sort(denominations.begin(), denominations.end(),
    [](int lhs, int rhs) { return lhs > rhs; });

  // if the lowest denom isn't 1... add 1.
  if (denominations.back() != 1)
    denominations.push_back(1);

  for (int coin: denominations) {
    int numCoins = N / coin;
    N %= coin;
    if (numCoins > 0)
      std::cout << numCoins << " x " << coin << '\n';
  }

    return 0;
}
