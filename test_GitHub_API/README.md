Для того, чтобы запустить test_api.py корректно - следуйте инструкции:
1. Зарегистрируйтесь на GitHub и перейдите в настройки (settings) для создания токена
2. Для получения токена перейдите в <> Developer settings --> Personal access tokens --> Tokens (classic) --> Generate new token --> Generate new token (classic)
3. Далее, укажите комментарий к токену и выберите возможности токена: repo и delete_repo, после чего нажмите Generate token
4. Скопируйте полученный токен, он вам понадобится в пункте 9
5. Установите Python (если не установлен) с официального сайта [python.org](https://www.python.org).
6. Откройте командную строку, склонируйте проект на компьютер и перейдите в папку с проектом:

   ```bash
   git clone https://github.com/barKoZZeR/test_tasks_E2E_and_GitHub.git
   cd test_tasks_E2E_and_GitHub
   cd test_GitHub_API
   
7. Создайте виртуальное окружение в командной строке:

   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **MacOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

8. Установите зависимости, используя команду:
   ```bash
   pip install -r requirements.txt

9. В папке "test_GitHub_API" создайте файл .env с данными вашего Git Hub аккаунта:

   ```bash
   USERNAME=github_username
   TOKEN=github_token
   REPOSITORY_NAME=name_of_repository
10. Запустите скрипт

    - **Windows**:
      ```bash
      python test_api.py
      ```

    - **Linux**:
      ```bash
      python3 test_api.py
      ```

    - **MacOS**:
      ```bash
      python3 test_api.py
      ```
   
После запуска скрипта вы получите уведомления о том, что репозиторий был создан, найден и удалён.