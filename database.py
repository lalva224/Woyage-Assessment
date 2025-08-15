from config import MONGO_URI,DATABASE_NAME
from models import File
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

#with motor asyncio we get higher scalability and concurrent request processing. Much more suited for big projects than pymongo.
async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DATABASE_NAME]
    #here it maps the beanie models to existing collections.
    await init_beanie(database=db,document_models=[File])
    return db
