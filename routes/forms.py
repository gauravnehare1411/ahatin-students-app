from fastapi import APIRouter, HTTPException, Depends
from models.form_models import ApplicationForm
from models.auth_models import User
from config.db import applications_collection
from schemas.auth_schema import get_current_user

router = APIRouter()

@router.post('/submit-application')
async def submit_application(data: ApplicationForm, current_user: User=Depends(get_current_user)):
    try:
        form_dict = data.dict()
        form_dict["userId"] = current_user.userId
        result = await applications_collection.insert_one(form_dict)
        return {"message": "Application saved successfully", "id": str(result.inserted_id)}
    
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to save application")