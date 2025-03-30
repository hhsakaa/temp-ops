# Temporal.io Python Workflow Setup

## Overview
This repository contains Python scripts to interact with a Temporal.io server, including workflow execution, worker setup, and client interaction.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pip
- Temporal server running (via Docker or Kubernetes)

## Installation

1. Clone the repository:
```sh
git clone <repository-url>
cd <repository-folder>
```

2. Create and activate a virtual environment (recommended):
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```sh
pip install temporalio asyncio
```

## Files
- `workflows.py`: Defines the Temporal workflow.
- `worker.py`: Runs the Temporal worker that listens for tasks.
- `start_workflow.py`: Executes the workflow via Temporal client.

## Running the Workflow

### 1. Start the Temporal Worker
Run the worker script to listen for tasks:
```sh
python worker.py
```

### 2. Execute the Workflow
Run the client script to trigger the workflow:
```sh
python start_workflow.py
```

## Expected Output
When running `start_workflow.py`, you should see an output like:
```
Workflow result: Hello, Akash from Temporal!
```

## Configuration
Update the Temporal server address in `start_workflow.py` and `worker.py` if needed:
```python
client = await Client.connect("your-server-ip:7233")
```

## Troubleshooting
- Ensure Temporal is running at the specified IP (`your-server-ip:7233`).
- If the worker is not picking up tasks, restart the worker.
- Use `docker ps` to verify that the Temporal containers are running.

## Contribution
Feel free to submit pull requests for improvements or fixes.

## License
This project is open-source and available under the MIT License.

