# FlightRadar24 FlightDiary Statistics
Quickly written code to analyze a flightradar24 flightdiary CSV file for repeat flights on a plane with the same registration.


### Usage
`python3 flightdiary_stats.py [path to flightdiary_...csv]`


**Sample output**
```
skipped entries missing registrations: 43

2022-02-03: UA2743 N75023 SNA - SFO Boeing 737 MAX 9 (B39M)
2023-03-09: UA2942 N75023 LAX - DEN Boeing 737 MAX 9 (B39M)

2023-02-07: UA549 N227UA SFO - EWR Boeing 777-200 (B772)
2023-11-03: UA35 N227UA SFO - KIX Boeing 777-200 (B772)

total number of registrations seen >1 time: 2
```


