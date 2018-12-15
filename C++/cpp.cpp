#include <iostream>
#include <fstream>

using namespace std;

int main(){

  ifstream ip("data.csv");

  if(!ip.is_open()) std::cout << "ERROR: File Open" << '\n';

  string Year;
  string CausesName;
  string CauseName;
  string State;
  string Deaths;
  string AgeadjustedDeathRate;
  string query;
  cout<<"Search By Year / Cause Name / State / Deaths / Age >> ";
  cin>>query;

  while(ip.good()){


    getline(ip,Year,',');
    getline(ip,CausesName,',');
    getline(ip,CauseName,',');
    getline(ip,State,',');
    getline(ip,Deaths,',');
    getline(ip,AgeadjustedDeathRate,',');


if(Year.find(query) != std::string::npos || CausesName.find(query) != std::string::npos || CauseName.find(query) != std::string::npos || State.find(query) != std::string::npos || Deaths.find(query) != std::string::npos || AgeadjustedDeathRate.find(query) != std::string::npos){

    std::cout << "133 Causes Name: "<<Year<< '\n';
    std::cout << "Cause Name: "<<CauseName<< '\n';
    std::cout << "State: "<<State << '\n';
    std::cout << "Deaths: "<<Deaths<< '\n';
    std::cout << "Age & Year: "<<AgeadjustedDeathRate<< '\n';

        cout<<"-----------------------------\n";

}

  }

  ip.close();
}
