from motor.motor_asyncio import AsyncIOMotorClient
from config.getenv_var import MONGO_URL

db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client.ahatin

users_collection = db.users
students_collection = db.students_data
verification_collection = db.verification_collection

applications_collection = db.applications

