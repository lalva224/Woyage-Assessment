from fastapi import APIRouter, HTTPException
from crud.search import search_file, read_s3_file
from models import APIResponse,FileResponse,File

router = APIRouter(prefix="/content/search")

@router.get("/",response_model=APIResponse)
async def search(search_term:str):
    """
    This endpoint calls crud files, first for retrieving the MongoDB Document (File). Then, for reading the contents
    """
    try:
        file:File = await search_file(search_term.lower())
        if not file:
            return APIResponse(
                result = "failure",
                message = "File Not Found!",
                data = None
            )
        content:str =await read_s3_file(file.file_path)
        print(content)
        fileResponse = FileResponse(file_path=file.file_path,file_content=content)
        api_response = APIResponse(
            result="success",
            message="File Found",
            data = fileResponse
            )
        return api_response
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


