import asyncio
from infrastructure import ingestion


async def main():
    await ingestion()


if __name__ == "__main__":
    asyncio.run(main())
