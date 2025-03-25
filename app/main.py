from fastapi import FastAPI
from app.kenburns import router as kenburns_router

app = FastAPI()

# Tích hợp router Ken Burns
app.include_router(kenburns_router)
