from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import get_settings
from database.db_client import init_db
from utils.logger import logger

from api.v1.routers.health import router as health_router
from api.v1.routers.auth import router as auth_router
from api.v1.routers.documents import router as documents_router
from api.v1.routers.chat import router as chat_router
from api.v1.routers.research import router as research_router
from api.v1.routers.admin import router as admin_router

settings = get_settings()

app = FastAPI(
    title="DocMind AI",
    description="AI Research & Synthesis Agent — Backend API",
    version=settings.APP_VERSION,
)

# ─── CORS ────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)

# ─── Routers ─────────────────────────────────────────────────
API_PREFIX = "/api/v1"

app.include_router(health_router, prefix=API_PREFIX)
app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(documents_router, prefix=API_PREFIX)
app.include_router(chat_router, prefix=API_PREFIX)
app.include_router(research_router, prefix=API_PREFIX)
app.include_router(admin_router, prefix=API_PREFIX)


# ─── Startup Event ───────────────────────────────────────────
@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting DocMind AI v{settings.APP_VERSION} [{settings.ENVIRONMENT}]")
    init_db()
    logger.info("Database tables initialized")
    # Phase 5: stale job recovery + retention cleanup will be added here
