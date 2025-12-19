from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.crypto import encrypt_message, decrypt_message

app = FastAPI()

class CryptoRequest(BaseModel):
    message: str
    password: str

@app.post("/encrypt")
async def encrypt(request: CryptoRequest):
    encrypted_message = encrypt_message(request.message, request.password)
    return JSONResponse(content={"result": encrypted_message})

@app.post("/decrypt")
async def decrypt(request: CryptoRequest):
    decrypted_message = decrypt_message(request.message, request.password)
    return JSONResponse(content={"result": decrypted_message})

app.mount("/", StaticFiles(directory="src/static", html = True), name="static")
