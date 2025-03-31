# Temporal.io with Docker Compose, Prometheus & Grafana

## Overview
This repository contains the setup for running Temporal.io with Docker Compose, along with monitoring using Prometheus and Grafana.

## Prerequisites
Ensure you have the following installed on your system:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <repository-url>
cd <repository-folder>
```

### 2. Set Environment Variables
Before running the setup, export the necessary environment variables:
```sh
export TEMPORAL_VERSION=1.21.0
export TEMPORAL_UI_VERSION=2.9.0
export TEMPORAL_ADMINTOOLS_VERSION=1.21.0
export ELASTICSEARCH_VERSION=7.10.2
export POSTGRESQL_VERSION=13
```

Alternatively, you can create a `.env` file and add the variables:
```
TEMPORAL_VERSION=1.21.0
TEMPORAL_UI_VERSION=2.9.0
TEMPORAL_ADMINTOOLS_VERSION=1.21.0
ELASTICSEARCH_VERSION=7.10.2
POSTGRESQL_VERSION=13
```

### 3. Start the Services
Run the following command to start Temporal, Prometheus, and Grafana:
```sh
docker-compose up -d
```
This will pull the necessary images and start the services in detached mode.

### 4. Verify Running Containers
Check if all containers are running:
```sh
docker ps
```

### 5. Access Temporal UI
Once the containers are up, access Temporal Web UI:
```
http://your-server-ip:8080/
```

### 6. Access Prometheus
Prometheus UI can be accessed at:
```
http://your-server-ip:9090/
```

### 7. Access Grafana
Grafana is available at:
```
http://localhost:3000/
```
(Default login: `admin` / `admin`)

## Monitoring Setup
### 8. Configure Prometheus
Prometheus is configured to scrape Temporal metrics from `temporal:8000`. If necessary, update `prometheus.yml`:
```yaml
scrape_configs:
  - job_name: 'temporal'
    static_configs:
      - targets: ['temporal:8000']
```
Restart Prometheus to apply changes:
```sh
docker-compose restart prometheus
```

### 9. Configure Grafana Dashboards
- Add Prometheus as a data source:
  1. Open Grafana and log in.
  2. Go to "Configuration" > "Data Sources".
  3. Add a new Prometheus data source with the URL: `http://prometheus:9090`
  4. Save and test the connection.
  5. Import pre-built Temporal dashboards for visualization.

### 10. Set Up Alerts in Grafana
To create alerts in Grafana:
1. Open Grafana and navigate to "Alerting" > "Rules".
2. Click "Create Alert Rule".
3. Set up conditions such as high workflow failures.
4. Configure notification channels (e.g., Slack, Email, Webhooks).

## Security Setup
### 11. Secure Temporal Services
- Use environment variables for credentials instead of hardcoding them.
- Restrict external access to Temporal services using firewall rules.
- Enable authentication for the Temporal UI.

### 12. Secure Prometheus & Grafana
- Set up authentication for Grafana dashboards.
- Limit Prometheus access to trusted IP addresses.
- Encrypt network traffic using TLS for secure communication.

### 13. Stopping the Services
To stop all running services:
```sh
docker-compose down
```

## Directory Structure
```
/
├── docker-compose.yml
├── prometheus.yml
├── README.md
└── workflows/
    ├── worker.py
    ├── workflows.py
    ├── start_workflow.py
```

## Troubleshooting
- If any container fails to start, check logs:
  ```sh
  docker-compose logs <container-name>
  ```
- If Temporal UI is not accessible, ensure that port `8080` is open.
- If Grafana is not displaying metrics, verify the Prometheus data source connection.

## Contribution
Feel free to submit issues or pull requests to improve this setup!

