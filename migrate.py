import asyncio
import typer

from db import engine, Base

cli = typer.Typer()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")


if __name__ == "__main__":
    cli()
