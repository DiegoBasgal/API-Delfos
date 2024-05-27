from fastapi import FastAPI, APIRouter

from views import signal_router, assets_router

app = FastAPI()
router = APIRouter()

app.include_router(signal_router)
app.include_router(assets_router)