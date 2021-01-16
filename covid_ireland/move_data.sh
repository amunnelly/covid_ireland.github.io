#!/bin/bash
FILE=~/Downloads/Covid19CountyStatisticsHPSCIreland.csv

if test -f "$FILE"; then

  rm data/Covid19CountyStatisticsHPSCIreland_.csv
  cp data/Covid19CountyStatisticsHPSCIreland.csv data/Covid19CountyStatisticsHPSCIreland_.csv
  mv ~/Downloads/Covid19CountyStatisticsHPSCIreland.csv data
  python national_plotter.py
  python covid_plotter.py

else
  read -p "You haven't downloaded the latest data. Hit enter to exit."
  exit 1

fi
