# Deploying Temporal.io on K3s with Prometheus & Grafana

## Overview
This guide explains how to deploy Temporal.io on a local K3s cluster with monitoring using Prometheus and Grafana.

## Prerequisites
Ensure you have the following installed:
- [K3s](https://k3s.io/) (Lightweight Kubernetes)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/)
- [Docker](https://www.docker.com/)

## 1. Install K3s
To install K3s on your local machine, run:
```sh
curl -sfL https://get.k3s.io | sh -
```

Verify the installation:
```sh
kubectl get nodes
```
If `kubectl` isn't working, export K3s' kubeconfig:
```sh
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

## 2. Install Helm
If you haven't installed Helm, install it using:
```sh
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

## 3. Deploy Temporal.io
### Add and Update Helm Repository
```sh
helm repo add temporal https://temporalio.github.io/helm-charts
helm repo update
```

### Install Temporal
```sh
helm install temporal temporal/temporal --namespace temporal --create-namespace
```

Verify that Temporal is running:
```sh
kubectl get pods -n temporal
```

## 4. Deploy Prometheus & Grafana
### Install Prometheus
```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace
```

### Install Grafana
```sh
helm install grafana prometheus-community/grafana --namespace monitoring
```

### Access Grafana
Retrieve admin password:
```sh
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

Forward the Grafana port to localhost:
```sh
kubectl port-forward svc/grafana 3000:80 -n monitoring
```
Now, open `http://localhost:3000/` in your browser and log in using admin credentials.

## 5. Deploy Temporal Worker
### Create a Worker Deployment
Create a `worker-deployment.yaml` file:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: temporal-worker
  namespace: temporal
spec:
  replicas: 1
  selector:
    matchLabels:
      app: temporal-worker
  template:
    metadata:
      labels:
        app: temporal-worker
    spec:
      containers:
      - name: worker
        image: your-worker-image
        env:
        - name: TEMPORAL_ADDRESS
          value: "temporal-frontend:7233"
```
Apply the deployment:
```sh
kubectl apply -f worker-deployment.yaml
```

## 6. Execute the Workflow
Run the Python script to start the workflow:
```sh
python start_workflow.py
```

## 7. Monitoring
- Temporal UI: `http://<K3S-IP>:8080`
- Prometheus: `http://<K3S-IP>:9090`
- Grafana: `http://localhost:3000/`

## Cleanup
To delete everything:
```sh
kubectl delete namespace temporal monitoring
```
To stop K3s:
```sh
sudo systemctl stop k3s
```
