#!/bin/bash

# Create Airflow Deployment
kubectl create deployment airflow --image=puckel/docker-airflow:latest

# Expose Airflow Service
kubectl expose deployment airflow --type=NodePort --port=8080 --target-port=8080