Для того, чтобы запустить test_E2E_UI.py корректно - следуйте инструкции:
1. Установите Python (если не установлен) с официального сайта [python.org](https://www.python.org).
2. Откройте командную строку, склонируйте проект на компьютер и перейдите в папку с проектом:

   ```bash
   git clone https://github.com/barKoZZeR/test_tasks_E2E_and_GitHub.git
   cd test_tasks_E2E_and_GitHub
   cd test_E2E_UI
   
3. Создайте виртуальное окружение в командной строке:

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

4. Установите Playwright, используя команду в командной строке:
   ```bash
   playwright install
5. По умолчанию тест запускается в браузере Chromium. Если вы хотите поменять браузер, то можете
изменить последнюю строку кода файла test_api.py (asyncio.run(test_purchase())), например:

   - **Firefox**:
     ```bash
     asyncio.run(test_purchase('firefox'))
     ```

   - **Safari**:
     ```bash
     asyncio.run(test_purchase('webkit'))
     ```
     
6. Запустите тест.
   - **Windows**:
     ```bash
     python test_E2E_UI.py
     ```

   - **Linux**:
     ```bash
     python3 test_E2E_UI.py
     ```

   - **MacOS**:
     ```bash
     python3 test_E2E_UI.py
     ```
   
После запуска скрипта вы получите уведомления о том, когда, во сколько и что было выполнено во время тестирования.