from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api.v1.router import router

app = FastAPI()
app.include_router(router, prefix="/api")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
async def read_root():
    return {"message": "Hello from FastAPI! Let's build a full stack app!"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 

    