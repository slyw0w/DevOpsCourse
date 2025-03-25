#!/bin/bash

# Create Superset Deployment
kubectl create deployment superset --image=amancevice/superset:latest

# Expose Superset Service
kubectl expose deployment superset --type=NodePort --port=8088 --name=superset-service