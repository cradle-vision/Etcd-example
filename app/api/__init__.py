from fastapi import APIRouter
from app.api.endpoints import deployment_points, cameras, edge_devices, playback_marker

api_router = APIRouter()
api_router.include_router(deployment_points.router, prefix="/deployment_points", tags=["deployment_points"])
api_router.include_router(cameras.router, prefix="/cameras", tags=["cameras"])
api_router.include_router(edge_devices.router, prefix="/edge_devices", tags=["edge_devices"])
api_router.include_router(playback_marker.router, prefix="/playback_marker", tags=["playback_marker"])
