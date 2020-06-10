#!/usr/bin/env bash

echo                "                  |=============================================|         "
echo                "                  |              Starting Service               |         "
echo                "                  |=============================================|         "
echo                "                  |1) kafka                                     |         "
echo                "                  |=============================================|         "
echo                "                  |2) Grafana                                   |         "
echo                "                  |=============================================|         "
echo                "                  |3) zookeper                                  |         "
echo                "                  |=============================================|         "
echo                "                  |4) Adminer                                   |         "
echo                "                  |=============================================|         "
echo                "                  |5) Msql                                      |         "
echo                "                  |=============================================|         "


docker-compose up &

sleep 200

echo                "                  |=============================================|         "
echo                "                  |              Starting Python                |         "
echo                "                  |=============================================|         "
echo                "                  |     ****  DataStream_producer ****          |         "
echo                "                  |                                             |         "
echo                "                  |=============================================|         "

python -m app.DataStream_producer &

sleep 10

echo                "                  |=============================================|         "
echo                "                  |              Starting Python                |         "
echo                "                  |=============================================|         "
echo                "                  |                                             |         "
echo                "                  |      ****   DataStream_consumer    ****     |         "
echo                "                  |=============================================|         "

python -m app.DataStream_consumer &