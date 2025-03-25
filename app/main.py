from fastapi import FastAPI
from app.kenburns import router as kenburns_router

app = FastAPI()
app.include_router(kenburns_router)
