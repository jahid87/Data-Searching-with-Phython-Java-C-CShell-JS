#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;


int main(){

    vector<string> timestamp(152644);
 //  vector<string> date(152644);
    vector<string> City(152644);
    vector<string> temperature(152644);
            vector<string> light(152644);
    vector<string> airquality(152644);
    vector<string> sound(152644);
    vector<string> humidity(152644);
      vector<string> dust(152644);

    int count = 0;
    string word;

    ifstream file("data.csv");

    if (!file.is_open())
        cerr << "File not found" << endl;

    while (file.good()){

        for (int i = 0; i < 152644; i++){

            getline(file, timestamp[i], ',');
     //       getline(file, date[i], ',');
            getline(file, City[i], ',');
            getline(file,temperature[i],',');
            getline(file, light[i], ',');
            getline(file, airquality[i], ',');
            getline(file, sound[i], ',');
            getline(file,humidity[i],',');
            getline(file,dust[i],'\n');
        }
    }

    cout << "Enter word: ";
    cin >> word;

    for (int j = 0; j < 152644; j++){
        if (City[j].find(word) != std::string::npos){
       //     cout << timestamp[j]<<" "<< City[j]<<" "<<temperature[j]<<" " << endl;
           std::cout << "timestamp: "<<timestamp[j]<< " " << '\n';
      std::cout << "City: "<<City[j] << '\n';
    std::cout << "temperature: "<<temperature[j]<< '\n';
    std::cout << "light: "<<light[j]<< '\n';
        std::cout << "airquality: "<<airquality[j]<< " " << '\n';
    std::cout << "sound: "<<sound[j]<< '\n';
    std::cout << "humidity: "<<humidity[j]<< '\n';
        std::cout << "dust: "<<dust[j]<< " "<< '\n';
        cout<<"-----------------------------\n";
            count++;
        }
    }

    cout << count;

    return 0;
}
