#!/bin/bash

# Create Airflow Deployment
kubectl create deployment airflow --image=puckel/docker-airflow:latest

# Expose Airflow Service
kubectl expose deployment superset --type=NodePort --port=8088 --name=airflow-service