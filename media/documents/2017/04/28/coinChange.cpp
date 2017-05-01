//Ashley Nguyen (apn2my)
//Homework 10 (Problem 1)
//CS 4102 ALGORITHMS
//Spring 2017
//On my honor, I have neither given nor received aid on this assignment

#include <iostream>
#include <cmath>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>

using namespace std;

//Assume coin denomination 1, 5, 10, 25
//Amount of money no more than 50
void coinDenomination(int amount){
  //int change;
  int check;
  int count=0;
  int Q=0, D=0, N=0, P=0;

    while(amount >= 25){
      count++;
      Q++;
      amount = amount - 25;
    }
    while(amount >= 10){
      count++;
      D++;
      amount = amount - 10;
    }
    while(amount >= 5){
      count++;
      N++;
      amount = amount - 5;
    }
    while(amount >= 1){
      count++;
      P++;
      amount = amount - 1;
    }

  if(Q == 0)
    cout << D << "x10¢, " << N << "x5¢, " << P << "x1¢";

  else if(N == 0)
    cout << Q << "x25¢, " << D << "x10¢, " << P << "x1¢";

  else if(D == 0)
    cout << Q << "x25¢, " << N << "x5¢, " << P << "x1¢";

  else if(P == 0)
    cout << Q << "x25¢, " << D << "x10¢, " << N << "x5¢";

  else
    cout << Q << "x25¢, " << D << "x10¢, " << N << "x5¢, " << P << " x 1¢";

}
void minChange(vector<vector<int> > C, int d[], int amount, int ds){
  //int k = (int) d.size();
  for(int i = 0; i < ds; i++){
    C[i][0] = 0;
  }

  for(int j = 0; j <= amount; j++){
    C[0][j] = j;
  }

  for(int i = 1; i < ds; i++){
    for(int j = 1; j <= amount; j++){
      if( j < d[i]){
        C[i][j] = C[i - 1][j];
      }
      else{
        C[i][j] = min( C[i-1][j] , 1 + C[i][j - d[i]] );
      }
    }
  }


//printing matrix
cout << endl;
cout << "The following shows the C[i][j] table computed. " << endl;
cout << endl;
cout << "C[i][j] ";
for(int i = 0; i <= amount; i++){
  cout << i << " ";
}
cout << endl;
for(int i = 0; i < ds; i++){
  for(int j = 0; j <= amount; j++){
    cout << C[i][j] << " ";
  }
  cout << endl;
}

}

  int main(){
    int coins[] =  {1, 5, 10, 25};
    int ds = sizeof(coins)/sizeof(coins[0]);

    int amount;
    cout << "Enter the amount of money in cents: ";
    cin >> amount;

    int d1, d2;

    //Coin denomination
    cout << endl << "Coin denominations determined: ";
    coinDenomination(amount);

    vector<vector <int> > C (4, vector<int>(amount));
    cout << endl;
    minChange(C, coins, amount, ds);
    return 0;

}
