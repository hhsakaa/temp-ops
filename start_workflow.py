from temporalio.client import Client
import asyncio

async def main():
    client = await Client.connect("34.228.166.199:7233")

    result = await client.execute_workflow(
        "MyWorkflow",
        "Akash",
        id="my-workflow-id",
        task_queue="my-task-queue",
    )
    print(f"Workflow result: {result}")

if __name__ == "__main__":
    asyncio.run(main())








