# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.core.config import settings
# from app.routers import menus

# app = FastAPI(title=settings.APP_NAME)

# app.add_middleware(
# CORSMiddleware,
# allow_origins=[""] if settings.ALLOWED_ORIGINS == "" else [settings.ALLOWED_ORIGINS],
# allow_credentials=True,
# allow_methods=[""],
# allow_headers=[""],
# )



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import menus

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
CORSMiddleware,
allow_origins=[""] if settings.ALLOWED_ORIGINS == "" else [settings.ALLOWED_ORIGINS],
allow_credentials=True,
allow_methods=[""],
allow_headers=[""],
)

app.include_router(menus.router, prefix="/api")
