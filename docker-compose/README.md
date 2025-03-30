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
http://34.228.166.199:8080/
```

### 6. Access Prometheus
Prometheus UI can be accessed at:
```
http://34.228.166.199:9090/
```

### 7. Access Grafana
Grafana is available at:
```
http://localhost:3000/
```
(Default login: `admin` / `admin`)

### 8. Configure Monitoring
- Prometheus is already set up to scrape Temporal metrics from `temporal:8000`.
- To configure Grafana, add Prometheus as a data source:
  1. Open Grafana and log in.
  2. Go to "Configuration" > "Data Sources".
  3. Add a new Prometheus data source with the URL: `http://prometheus:9090`
  4. Save and test the connection.
  5. Import dashboards to visualize Temporal metrics.

### 9. Stopping the Services
To stop all running services:
```sh
docker-compose down
```

## Directory Structure
```
/
├── docker-compose.yml
├── prometheus.yml
└── README.md
```

## Troubleshooting
- If any container fails to start, check logs:
  ```sh
  docker-compose logs <container-name>
  ```
- If Temporal UI is not accessible, ensure that port `8080` is open.
- If Grafana is not displaying metrics, verify the Prometheus data source connection.

## Contribution
Feel free to submit pull requests for improvements or fixes.

## License
This project is open-source and available under the MIT License.

