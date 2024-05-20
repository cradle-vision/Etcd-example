import etcd3
from app.core.config import settings


def get_etcd_client():
    try:
        etcd = etcd3.client(host=settings.ETCD_HOST, port=settings.ETCD_PORT)
        etcd.status()
        return etcd
    except Exception as e:
        print(f"Ошибка подключения к etcd: {e}")
        return None
