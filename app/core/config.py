import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    ETCD_HOST: str = os.getenv("ETCD_HOST", "127.0.0.1")
    ETCD_PORT: int = int(os.getenv("ETCD_PORT", 2379))


settings = Settings()
