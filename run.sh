#!/usr/bin/env bash

echo "|=============================================|"
echo "|              Starting Service               |"
echo "|=============================================|"
echo "|1) kafka                                     |"
echo "|=============================================|"
echo "|2) Grafana                                   |"
echo "|=============================================|"
echo "|3) zookeper                                  |"
echo "|=============================================|"
echo "|4) Adminer                                   |"
echo "|=============================================|"
echo "|5) Msql                                      |"
echo "|=============================================|"


docker-compose up &

sleep 3m

echo "|=============================================|"
echo "|              Starting Python                |"
echo "|=============================================|"
echo "| **** DataStream_producer                    |"
echo "|                                             |"
echo "|      *********** DataStream_consumer        |"
echo "|=============================================|"

python -m app.DataStream_producer &
python -m app.DataStream_consumer &