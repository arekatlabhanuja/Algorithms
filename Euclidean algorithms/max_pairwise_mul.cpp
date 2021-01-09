#include <cstdlib>
#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>

int64_t MaxPairwiseProduct(const std::vector<int64_t>& numbers) {

    int n = numbers.size();


int maxind1=-1;
for (int i=0; i<n; i++)
{
    if(maxind1==-1 || numbers[i]>numbers[maxind1])
        maxind1=i;
}
int maxind2=-1;
for (int j=0; j<n; j++)
   {

    if(j!=maxind1 && (maxind2==-1 || numbers[j]>numbers[maxind2]))
    maxind2=j;}
int64_t restult=numbers[maxind1]*numbers[maxind2];
    return restult;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int64_t> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }
    cout << MaxPairwiseProduct(numbers) << "\n";
return 0;}