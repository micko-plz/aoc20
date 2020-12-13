#include <iostream>
#include <vector>

int main() {

    std::vector<int> buses{13 ,17 ,19 ,23 ,29 ,37 ,41 ,379 ,557};
    std::vector<int>  times = {54 ,58 ,91 ,49 ,70 ,35 ,0 ,41 ,72};
    std::vector<int>  iter = {7 ,6 ,5 ,4 ,3 ,2 ,1 ,0};

    int nBuses = buses.size();
    unsigned long long int t = (100000000000000 /  buses[nBuses-1]) * buses[nBuses-1]  - times[nBuses-1];

    bool done = false; 
    while (!done) {
      done = true;
      for (int i = 0; i < iter.size(); ++i) {
        if ((t + times[iter[i]]) % buses[iter[i]] == 0) {
          // do nothing
        } else {
          t += buses[nBuses-1];
          done = false;
        }
      }
    }

    std::cout << t << std::endl;
}