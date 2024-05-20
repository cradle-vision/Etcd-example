from fastapi import APIRouter, HTTPException
from app.core.etcd_client import get_etcd_client

router = APIRouter()


@router.post("/create_deployment_point/{deployment_point_id}")
def create_deployment_point(deployment_point_id: str):
    etcd = get_etcd_client()
    if etcd is None:
        raise HTTPException(
            status_code=500,
            detail="Не удалось подключиться к etcd серверу"
        )

    etcd.put(f"{deployment_point_id}/", "")
    return {"message": f"Deployment point {deployment_point_id} created"}
