from tortoise import Tortoise

from config import config


async def db_init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(db_url=config["db_url"], modules={"models": ["moboard.models"]})
    # Generate the schema
    await Tortoise.generate_schemas(safe=True)
