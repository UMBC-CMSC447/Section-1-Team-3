#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <sqlite3.h>
using namespace std;

int main () {
  ofstream myfile;
  float price;
  int rating;
  string styles[] = {"Villa", "Modern", "Cottage", "Condo", "Ranch", "Victorian"};
  myfile.open ("dataset.txt");
  for (int i = 0; i < 10; i++){
    rating = rand() % 5;
    price = (rand() % 10 + 1) * 10000;
    myfile << "{ \n";
    myfile << "image : \"image0"  << i << ".png\", \n";
    myfile << "style : \""  << styles[i%6] << "\", \n";
    myfile << "timeslot : \""  << i << "\", \n";
    myfile << "price : \""  << price << "\", \n";
    myfile << "rating : \""  << rating << "\", \n";
    myfile << "} \n";
  }
  myfile.close();
  return 0;
}
