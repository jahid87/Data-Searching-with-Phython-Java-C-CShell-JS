#include<stdio.h>
#include<sstream>
#include <iostream>
#include <string.h>
#include <fstream>
#include <vector>
#include <sstream>



using namespace std;
string choice()
{

    cout << "Enter your choice" << endl;
    cout << "1. city-wise search" << endl;
    cout << "2. parameter-wise search" << endl;
    cout << "3. date-wise search" << endl;
    cout << "4. year-wise search" << endl;
    cout << "5. month-wise search" << endl;
    cout << "6. Exit" << endl;

    string op;
    cout << "Enter you choice: ";
    getline(cin, op);
    cout << endl;

    if (op[op.length()-1] == '\n')
        op.erase(op.length()-1);

    return op;
}

int main()
{
    ifstream ip("data.csv");
    if(!ip.is_open())
        cout << "File not found" << '\n';

    string varDate, varCity, varTemperature, varLight, varAirQuality, varSound, varHumidity, varDust;
    vector <string> date;
    vector <string> city;
    vector <string> temperature;
    vector <string> light;
    vector <string> airquality;
    vector <string> sound;
    vector <string> humidity;
    vector <string> dust;

    int cnt = 0;
    while(ip.good())
    {
        getline(ip, varDate, ',');
        getline(ip, varCity, ',');
        getline(ip, varTemperature, ',');
        getline(ip, varLight, ',');
        getline(ip, varAirQuality, ',');
        getline(ip, varSound, ',');
        getline(ip, varHumidity, ',');
        getline(ip, varDust, '\n');

        date.push_back(varDate);
        city.push_back(varCity);
        temperature.push_back(varTemperature);
        light.push_back(varLight);
        airquality.push_back(varAirQuality);
        sound.push_back(varSound);
        humidity.push_back(varHumidity);
        dust.push_back(varDust);


        cnt++;
        if(cnt == 20)
            break;
    }


    for(int i=0; i<20; i++)
    {
        cout << date[i] << " " << city[i] << " " << temperature[i] << " " << light[i] << " " << airquality[i] << " " << sound[i] << " " << humidity[i] << " " << dust[i] << endl;
    }

    while(1)
    {
        string option = choice();

        if(option == "1")
        {
            string user_city;
            cout << "Input a city name: ";
            getline(cin, user_city);

            for(int i=0; i<city.size(); i++)
            {
                if(user_city == city[i])
                {
                    cout << city[i] << " " << temperature[i] << " " << light[i] << " " << airquality[i] << " " << sound[i] << " " << humidity[i] << " " << dust[i] << endl;
                }
            }
            cout << endl;
        }
        else if(option == "2")
        {
            string para;
            cout << "Input a parameter name: ";
            getline(cin, para);

            if (para.compare(temperature[0])==0)
            {
                for(int i=1; i<temperature.size(); i++)
                {
                    cout << temperature[i] << endl;
                }
            }
            else if (para.compare(light[0])==0)
            {
                for(int i =1; i<light.size(); i++)
                {
                    cout << light[i] << endl;
                }
            }
            else if (para.compare(airquality[0])==0)
            {
                for(int i =1; i<airquality.size(); i++)
                {
                    cout << airquality[i] << endl;
                }
            }
            else if (para.compare(sound[0])==0)
            {
                for(int i =1; i<sound.size(); i++)
                {
                    cout << sound[i] << endl;
                }
            }
            else if (para.compare(humidity[0])==0)
            {
                for(int i =1; i<humidity.size(); i++)
                {
                    cout << humidity[i] << endl;
                }
            }
            else if (para.compare(dust[0])==0)
            {
                for(int i =1; i<dust.size(); i++)
                {
                    cout << dust[i] << endl;
                }
            }
            else
            {
                cout << "Invalid Input" << endl;
            }
            cout << endl;
        }
        else if(option == "3")
        {
            string user_date;
            cout << "Enter a date: ";
            getline(cin, user_date);

            for(int i=0; i<date.size(); i++)
            {
                string timestamp = date[i];
                string original_date = timestamp.substr(0,10);

                if(original_date == user_date)
                {
                    cout << original_date << " " << city[i] << " " << temperature[i] << " " << light[i] << " " << airquality[i] << " " << sound[i] << " " << humidity[i] << " " << dust[i] << endl;

                }
            }
            cout << endl;
        }
        else if(option == "4")
        {
            string year;
            cout << "Enter a year: ";
            getline(cin, year);

            for(int i=0; i<date.size(); i++)
            {
                string timestamp = date[i];
                string org_year = timestamp.substr(0,4);

                if(org_year == year)
                {

                    cout << org_year << " " << city[i] << " " << temperature[i] << " " << light[i] << " " << airquality[i] << " " << sound[i] << " " << humidity[i] << " " << dust[i] << endl;
                }
            }
            cout << endl;
        }
        else if(option == "5")
        {
            string user_month;
            cout << "Enter a month: ";
            getline(cin, user_month);

            for(int i=0; i<date.size(); i++)
            {
                string timestamp = date[i];
                string org_month = timestamp.substr(5,2);

                if(org_month == user_month)
                {
                    cout << org_month << " " << city[i] << " " << temperature[i] << " " << light[i] << " " << airquality[i] << " " << sound[i] << " " << humidity[i] << " " << dust[i] << endl;
                }
            }
            cout << endl;
        }
        else if(option == "6")
        {
            break;
        }
        else
        {
           cout << "Invalid Option\n" << endl;
        }

    }

    return 0;
}
