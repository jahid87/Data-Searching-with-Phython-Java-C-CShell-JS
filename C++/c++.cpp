#include <iostream>
#include <fstream>

using namespace std;

int main(){

  ifstream ip("data.csv");

  if(!ip.is_open()) std::cout << "ERROR: File Open" << '\n';

  string year;
  string State;
  string Deaths;

  cout<<"enter year ";
  cin>>query;

  while(ip.good()){


    getline(ip,year,',');
    getline(ip,133 Cause Name,',');
    getline(ip,Cause Name,',');
    getline(ip,State,',');
        getline(ip,Deaths,',');
    getline(ip,Age-adjusted Death Rate,',');


if(year.find(query) != std::string::npos|| State.find(query) != std::string::npos){

    std::cout << "year: "<<year<< " "<<133 Cause Name << '\n';
      std::cout << "133 Cause Name: "<<133 Cause Name << '\n';
    std::cout << "Cause Name: "<<Cause Name << '\n';
    std::cout << "State: "<<State << '\n';
        std::cout << "Deaths: "<<Deaths<< " "<<133 Cause Name << '\n';
    std::cout << "Age-adjusted Death Rate: "<<Age-adjusted Death Rate << '\n';
    std::cout << "humidity: "<<humidity << '\n';
        std::cout << "dust: "<<dust<< " "<< '\n';
        cout<<"-----------------------------\n";

}

  }

  ip.close();
}
