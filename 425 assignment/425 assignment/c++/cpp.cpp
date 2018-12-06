#include <iostream>
#include <fstream>

using namespace std;

int main(){

  ifstream ip("data.csv");

  if(!ip.is_open()) std::cout << "ERROR: File Open" << '\n';

  string timestamp;
  string date;
  string City;
  string temperature;
     string light;
  string airquality;
  string sound;
  string humidity;
  string dust;
  string query;
  cout<<"enter City Name or Date(xxxx-xx-xx) or Month(xxxx-xx) or Year(xxx):";
  cin>>query;

  while(ip.good()){


    getline(ip,timestamp,',');
    getline(ip,City,',');
    getline(ip,temperature,',');
    getline(ip,light,',');
        getline(ip,airquality,',');
    getline(ip,sound,',');
    getline(ip,humidity,',');
    getline(ip,dust,'\n');

if(City.find(query) != std::string::npos || timestamp.find(query) != std::string::npos){

    std::cout << "timestamp: "<<timestamp<< " "<< '\n';
      std::cout << "City: "<<City << '\n';
    std::cout << "temperature: "<<temperature << '\n';
    std::cout << "light: "<<light << '\n';
        std::cout << "airquality: "<<airquality<< " "<< '\n';
    std::cout << "sound: "<<sound << '\n';
    std::cout << "humidity: "<<humidity << '\n';
        std::cout << "dust: "<<dust<< " "<< '\n';
        cout<<"-----------------------------\n";

}

  }

  ip.close();
}
