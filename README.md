# Etcd-example

## Установка

### Локальная установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/yourusername/etcd-example.git
    cd etcd-example
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Запустите приложение:

    ```sh
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

Приложение будет доступно по адресу `http://localhost:8000`.

### Запуск с помощью Docker

1. Убедитесь, что у вас установлены Docker и Docker Compose.

2. Пересоберите и запустите контейнеры:

    ```sh
    docker-compose up --build
    ```

Приложение будет доступно по адресу `http://localhost:8000`.

## API эндпоинты

### Deployment Points

- **Создать точку развертывания**
    - **URL:** `/deployment_points/create_deployment_point/{deployment_point_id}`
    - **Метод:** `POST`

### Cameras

- **Создать камеру**
    - **URL:** `/cameras/create_camera/{deployment_point_id}/{camera_id}`
    - **Метод:** `POST`
    - **Параметры:**
        - `rtsp_uri`: строка, содержащая URI потока RTSP

- **Установить ROI для камеры**
    - **URL:** `/cameras/set_camera_roi/{deployment_point_id}/{camera_id}`
    - **Метод:** `POST`
    - **Параметры:**
        - `roi_data`: JSON массив с данными ROI

### Edge Devices

- **Назначить Edge Device для камеры**
    - **URL:** `/edge_devices/assign_edge_device/{deployment_point_id}/{camera_id}/{edge_device_id}`
    - **Метод:** `POST`

### Playback Marker

- **Установить маркер воспроизведения для камеры**
    - **URL:** `/playback_marker/set_playback_marker/{deployment_point_id}/{camera_id}`
    - **Метод:** `POST`
    - **Параметры:**
        - `ttl`: (по умолчанию 60 секунд)

## Переменные окружения

Создайте файл `.env` в корне проекта и добавьте следующие переменные:
    - 
    -
