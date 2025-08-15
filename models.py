from beanie import Document
from pydantic import BaseModel

#beanie model for mapping with existing collections in db
class File(Document):
    name: str
    file_path:str

#pydantic output models.
class FileResponse(BaseModel):
    file_path:str
    file_content:str

class APIResponse(BaseModel):
    result:str
    message:str
    data: FileResponse | None