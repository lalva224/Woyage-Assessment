from config import s3_client,BUCKET_NAME
from models import FileResponse,File


#reads s3 file given the file_path.
async def read_s3_file(file_path: str) -> str:
    try:
        #key is only the last part of file path. Set previous part to blank.
        key = file_path.replace(f"s3://{BUCKET_NAME}/", "")
        obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=key)
        content = obj["Body"].read().decode("utf-8")
        return content
    except s3_client.exceptions.NoSuchKey:
        return None
    except Exception as e:
        print(f"Error reading S3 file: {e}")
        return None
#searches mongoDB, using beanie model, for matching search term.
async def search_file(search_term:str)->File | None:
    file = await File.find_one({"name":search_term})
    print(file)
    return file

