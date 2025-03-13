#!/bin/bash
docker build -t homeassignment9 .
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker run homeassignment9