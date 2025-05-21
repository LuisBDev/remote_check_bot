from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query, HTTPException


app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check_health")
def check_health(key: str = Query(...)):
    if key == "ultra_secret_key":
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=403, detail="not ok")