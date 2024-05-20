from fastapi import APIRouter, HTTPException
from app.core.etcd_client import get_etcd_client

router = APIRouter()


@router.post("/set_playback_marker/{deployment_point_id}/{camera_id}")
def set_playback_marker(deployment_point_id: str, camera_id: str, ttl: int = 60):
    etcd = get_etcd_client()
    if etcd is None:
        raise HTTPException(status_code=500, detail="Не удалось подключиться к etcd серверу")

    lease = etcd.lease(ttl)
    etcd.put(f"{deployment_point_id}/{camera_id}/Playback_Marker", "", lease=lease)
    return {
        "message": f"Playback marker set for camera {camera_id} in "
                   f"deployment point {deployment_point_id} with TTL {ttl} seconds"
    }
