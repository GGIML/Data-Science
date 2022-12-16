#!/usr/bin/env bash

echo "***********************************"
echo "Starting Mlflow Server"
mlflow server --host 0.0.0.0 \
              --default-artifact-root gs://mlflow-demo-vivadata \
              --backend-store-uri file:gs://mlflow-demo-vivadata \
              --port 5000
