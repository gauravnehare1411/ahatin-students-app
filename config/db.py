from motor.motor_asyncio import AsyncIOMotorClient
from config.getenv_var import MONGO_URL

db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client.ahatin

users_collection = db.users
verification_collection = db.verification_collection
applications_collection = db.applications
deleted_users_collection = db.deleted_users
deleted_applications_collection = db.deleted_applications

