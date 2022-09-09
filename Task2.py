import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на Яндекс.Диск"""
        # Определяем запрос для получения ссылки согласно документации Yandex.API
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        # Выделяем имя загружаемого файла
        filename = file_path.split('/', )[-1]
        # Определяем формат заголовков запроса
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        # Определяем параметры запроса (назначаем путь загрузки, имя файла и разрешаем перезапись)
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        # Выполняем запрос на получение ссылки для загрузки
        response = requests.get(upload_url, headers=headers, params=params).json()
        # Выделяем ссылку для загрузки в отдельную переменную
        href = response.get("href", "")
        # Выполняем запрос на загрузку файла на Яндекс.Диск по полученной ссылке
        responce = requests.put(href, data=open(file_path, 'rb'))
        # Получаем статус отправки файла
        responce.raise_for_status()
        # Проверяем успешность отправки по полученному статусу
        if responce.status_code == 201:
            return 'Файл загружен успешно'
        else:
            return f"Ошибка загрузки файла! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    # Получаем путь к загружаемому файлу и токен от пользователя
    path_to_file = f'E:/upload/eclipse-inst-jre-win64.exe'
    token = ''
    # Определяем экземпляр класса для токена пользователя
    uploader = YaUploader(token)
    # Загружаем файл на диск
    print(f"Файл {path_to_file.split('/', )[-1]} загружается на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)