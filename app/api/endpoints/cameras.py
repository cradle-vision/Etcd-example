from fastapi import APIRouter, HTTPException
import json
from app.core.etcd_client import get_etcd_client

router = APIRouter()


@router.post("/create_camera/{deployment_point_id}/{camera_id}")
def create_camera(deployment_point_id: str, camera_id: str, rtsp_uri: str):
    etcd = get_etcd_client()
    if etcd is None:
        raise HTTPException(status_code=500, detail="Не удалось подключиться к etcd серверу")

    camera_json = {
        "rtsp_uri": rtsp_uri
    }
    etcd.put(f"{deployment_point_id}/{camera_id}/", json.dumps(camera_json))
    return {"message": f"Camera {camera_id} created in deployment point {deployment_point_id}"}


@router.post("/set_camera_roi/{deployment_point_id}/{camera_id}")
def set_camera_roi(deployment_point_id: str, camera_id: str, roi_data: list):
    etcd = get_etcd_client()
    if etcd is None:
        raise HTTPException(status_code=500, detail="Не удалось подключиться к etcd серверу")

    etcd.put(f"{deployment_point_id}/{camera_id}/Camera_ROI", json.dumps(roi_data))
    return {"message": f"ROI set for camera {camera_id} in deployment point {deployment_point_id}"}
