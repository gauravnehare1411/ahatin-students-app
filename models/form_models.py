from pydantic import BaseModel
from typing import List, Optional

class HighestQualification(BaseModel):
    type: str
    school: str
    board: str
    year: str
    percentage: str

class PreviousQualification(BaseModel):
    type: str
    school: str
    board: str
    year: str
    percentage: str

class Educational(BaseModel):
    highestQualification: HighestQualification
    previousQualifications: List[PreviousQualification] = []

class StudyPreferences(BaseModel):
    preferredCountry: str
    preferredCourse: str
    preferredIntakeMonth: str
    preferredIntakeYear: str
    degreeLevel: str
    preferredUniversities: Optional[str] = None

class Scores(BaseModel):
    ielts: Optional[str] = None
    toefl: Optional[str] = None
    pte: Optional[str] = None

class Certifications(BaseModel):
    hasCertifications: bool
    scores: Optional[Scores] = None

class Experience(BaseModel):
    jobTitle: str
    isRelated: str
    companyName: str
    years: str

class WorkExperience(BaseModel):
    hasExperience: bool
    experience: Optional[Experience] = None

class FinancialInformation(BaseModel):
    estimatedBudget: str
    sourceOfFunding: str

class ApplicationForm(BaseModel):
    educational: Educational
    studyPreferences: StudyPreferences
    certifications: Certifications
    workExperience: WorkExperience
    financialInformation: FinancialInformation

class StatusUpdate(BaseModel):
    status: str