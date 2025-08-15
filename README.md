# Woyage Assessment - FastAPI S3 File Search

A FastAPI application that provides an endpoint to search for files in MongoDB and read their contents from Amazon S3.

## Features

- **MongoDB Integration**: Search for files using MongoDB as the database
- **S3 File Reading**: Retrieve file contents directly from Amazon S3
- **RESTful API**: Clean and simple API endpoint for file search
- **Async Operations**: Built with async/await for better performance
- **Environment Configuration**: Secure configuration management using environment variables

## Project Structure

```
woyage-assessment/
├── main.py              # FastAPI application entry point
├── config.py            # Configuration and environment variables
├── database.py          # MongoDB connection and initialization
├── models.py            # Data models and Pydantic schemas
├── requirements.txt     # Python dependencies
├── routers/
│   └── search.py       # API router for search functionality
├── crud/               # Database operations
└── venv/               # Virtual environment
```

## Prerequisites

- Python 3.8+
- MongoDB instance
- Amazon AWS account with S3 access
- AWS credentials (Access Key, Secret Key)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd woyage-assessment
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:
   ```env
   MONGO_URI=""
   COLLECTION_NAME=""
   AWS_ACCESS_KEY=""
   AWS_SECRET_KEY=""
   AWS_REGION=""
   BUCKET_NAME=""
   ```

5. **Set up MongoDB database**
   - Ensure MongoDB is running
   - Create a collection called `File` with documents containing `name` and `file_path` fields
   - Write MONGO_URI and DATABASE_NAME

## Running the Application

1. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Documentation

### Search Endpoint

**GET** `/content/search/`

Search for a file by name and retrieve its content from S3.

**Query Parameters:**
- `search_term` (string, required): The name of the file to search for

**Response Format:**
```json
{
  "result": "success",
  "message": "File Found",
  "data": {
    "file_path": "s3://bucket/path/to/file.txt",
    "file_content": "File content here..."
  }
}
```

**Error Response:**
```json
{
  "result": "failure",
  "message": "File Not Found!",
  "data": null
}
```

## Database Schema

The MongoDB collection should contain documents with the following structure:
```json
{
  "name": "filename.txt",
  "file_path": "s3://bucket-name/path/to/filename.txt"
}
```

