//Ashley Nguyen (apn2my)
//Homework 10 (Problem 2)
//CS 4102 ALGORITHMS
//Spring 2017
//On my honor, I have neither given nor received aid on this assignment

#include <iostream>
#include <algorithm>

using namespace std;

struct Job{
   int id;
   int dead;
   int profit;
};

bool isFeasible(Job x, Job y){
    if(x.dead == y.dead){
      return (x.profit > y.profit ? true : false);
    }
    return (x.dead < y.dead ? true : false);

}

bool sortJob(Job x, Job y){
     return (x.profit > y.profit);
}

void printJobScheduling(Job jobs[], int n){
    sort(jobs, jobs+n, sortJob);

    int result[n];
    bool slot[n];

    for (int i = 0; i<n; i++)
        slot[i] = false;

    for (int i = 0; i < n; i++){
       for (int j = min(n, jobs[i].dead)-1; j >= 0; j--){

          // Feasbility check
          if (slot[j] == false){
             result[j] = i;
             slot[j] = true;
             break;
          }
       }
    }

    // Print the result
    cout << "[";
    for (int i = 0; i < n; i++){
       if (slot[i]){
         cout  << jobs[result[i]].id  << " ";
       }
     }
     cout << "]";

    //sum profit
    int total = 0;
    for(int i = 0; i < n; i++){
      if(slot[i]){
        total += jobs[result[i]].profit;
      }
    }
  cout << " is a feasible sequence with maximum total profit of " << total << endl;
}


int main(){
    cout << "Enter the total number of jobs: ";
    int num;
    cin >> num;
    int prof[num], deadline[num];
    Job s[num];

    for (int i = 0; i < num; i++){
        cout << "Enter the deadline and profit for job " << i+1 << ": ";
        cin >> deadline[i];
        cin >> prof[i];
        Job x = {i+1, deadline[i], prof[i]};
        s[i] = x;
    }

    int size = sizeof(s)/sizeof(s[0]);
    //Answer: [7, 3, 5] is a feasible sequence with maximum total profit of 100
    cout << "Answer: ";
    printJobScheduling(s, size);


    return 0;
}
