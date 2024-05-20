from fastapi import APIRouter, HTTPException
from app.core.etcd_client import get_etcd_client

router = APIRouter()


@router.post("/assign_edge_device/{deployment_point_id}/{camera_id}/{edge_device_id}")
def assign_edge_device(deployment_point_id: str, camera_id: str, edge_device_id: str):
    etcd = get_etcd_client()
    if etcd is None:
        raise HTTPException(status_code=500, detail="Не удалось подключиться к etcd серверу")

    etcd.put(f"{deployment_point_id}/{camera_id}/Edge_Device", edge_device_id)
    return {
        "message": f"Edge device {edge_device_id} assigned to "
                   f"camera {camera_id} in deployment point {deployment_point_id}"}
