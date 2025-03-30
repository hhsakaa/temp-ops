# Deploying Temporal.io on Amazon EKS with Prometheus & Grafana

## Overview
This guide covers deploying Temporal.io on Amazon Elastic Kubernetes Service (EKS) with monitoring using Prometheus and Grafana.

## Prerequisites
Ensure you have the following installed:
- [AWS CLI](https://aws.amazon.com/cli/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [eksctl](https://eksctl.io/)
- [Helm](https://helm.sh/)
- An AWS account with IAM permissions to create EKS clusters

## 1. Create an EKS Cluster
Run the following command to create an EKS cluster:
```sh
eksctl create cluster --name temporal-cluster --region us-east-1 --nodegroup-name workers --node-type t3.medium --nodes 2
```

Verify the cluster is running:
```sh
kubectl get nodes
```

## 2. Deploy Temporal.io
### Install Temporal using Helm
```sh
helm repo add temporal https://temporalio.github.io/helm-charts
helm repo update
helm install temporal temporal/temporal --namespace temporal --create-namespace
```

Verify the deployment:
```sh
kubectl get pods -n temporal
```

## 3. Deploy Prometheus for Monitoring
### Install Prometheus using Helm
```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace
```

Verify Prometheus:
```sh
kubectl get pods -n monitoring
```

## 4. Deploy Grafana for Visualization
### Install Grafana using Helm
```sh
helm install grafana prometheus-community/grafana --namespace monitoring
```

Retrieve Grafana credentials:
```sh
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

Port-forward Grafana to access it:
```sh
kubectl port-forward svc/grafana 3000:80 -n monitoring
```

Access Grafana at `http://localhost:3000/` and configure Prometheus as a data source.

## 5. Deploy Temporal Workflows
### Apply Kubernetes Configurations
Create a `worker-deployment.yaml` file to deploy the Temporal worker:
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

### Start the Workflow Execution
Use the `start_workflow.py` script to trigger the workflow:
```sh
python start_workflow.py
```

## 6. Monitoring
- Access Temporal UI: `http://<EKS-LOADBALANCER-IP>:8080`
- Access Prometheus: `http://<EKS-LOADBALANCER-IP>:9090`
- Access Grafana: `http://localhost:3000/`

## Cleanup
To delete the cluster and all resources:
```sh
eksctl delete cluster --name temporal-cluster
```

## Contribution
Feel free to submit pull requests for improvements.

## License
This project is open-source and available under the MIT License.

