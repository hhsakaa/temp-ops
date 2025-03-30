from temporalio.worker import Worker
from temporalio.client import Client
import asyncio
from workflows import MyWorkflow

async def main():
    print("Starting Temporal Worker...")
    client = await Client.connect("34.228.166.199:7233")

    worker = Worker(
        client,
        task_queue="my-task-queue",
        workflows=[MyWorkflow]
    )
    print("Worker is now listening for tasks...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())




