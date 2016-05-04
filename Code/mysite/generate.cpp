#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <sqlite3.h>
#include <math.h>
using namespace std;

int main () {
  ofstream myfile;
  float price;
  float lat = 38.386983;
  float Long = -75.064957;
  float flip;
  string loc = "Ocean-City";
  string styles[] = {"Villa", "Modern", "Cottage", "Condo", "Ranch", "Victorian"};
  string filename = loc + ".txt";
  const char* file = filename.c_str();
  myfile.open (file);
  for (int i = 0; i < 23; i++){
    flip = rand()%2;
    float variance = ((float)rand())/(float)((RAND_MAX/10.0));
    variance /= 1000.0;
    if (flip > 0){
      variance *= -1;
    }
    price = (rand() % 10 + 1) * 10000;
    myfile << loc <<"house0" << i << "\n";
    myfile << price << "\n";
    myfile << loc << "\n";
    myfile << "ImageTest0" << abs(rand()%25) << ".jpg" << "\n";
    myfile << "This is example " << loc <<" house number " << i << " in " << loc << "\n";
    myfile << lat+variance << "\n";
    myfile << Long+variance << "\n";
  }
  
  myfile.close();
  return 0;
}
