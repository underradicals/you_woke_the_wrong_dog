import asyncio
from infrastructure import ingestion, image_ingestion


async def main() -> None:
    await ingestion()
    await image_ingestion()


if __name__ == "__main__":
    asyncio.run(main())
