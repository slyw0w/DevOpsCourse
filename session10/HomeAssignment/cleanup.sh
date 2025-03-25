#!/bin/bash

# Delete Superset resources
kubectl delete deployment superset
kubectl delete service superset-service

# Delete Airflow resources
kubectl delete deployment airflow
kubectl delete service airflow-service