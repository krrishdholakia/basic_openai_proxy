# import sys, os
# sys.path.insert(
#     0, os.path.abspath("../")
# )  # Adds the parent directory to the system path
from fastapi import FastAPI, Request, status, HTTPException, Depends
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException, UploadFile, File
import httpx, os, json
from openai import AsyncOpenAI
from typing import Optional

class ProxyException(Exception):
    # NOTE: DO NOT MODIFY THIS
    # This is used to map exactly to OPENAI Exceptions
    def __init__(
        self,
        message: str,
        type: str,
        param: Optional[str],
        code: Optional[int],
    ):
        self.message = message
        self.type = type
        self.param = param
        self.code = code

    def to_dict(self) -> dict:
        """Converts the ProxyException instance to a dictionary."""
        return {
            "message": self.message,
            "type": self.type,
            "param": self.param,
            "code": self.code,
        }



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = AsyncOpenAI(api_key="sk-1234", base_url="https://exampleopenaiendpoint-production.up.railway.app/")

# for completion
@app.post("/chat/completions")
@app.post("/v1/chat/completions")
async def completion(request: Request):
    body = await request.body()
    data = json.loads(body.decode())
    return await client.chat.completions.create(**data)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000, workers=4)
