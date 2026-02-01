# AT Lessons (Stepik)

Обучаюсь авто-тестированию с помощью курсов на Stepik.<br>
Ссылка на курс: https://stepik.org/course/575 (курс бесплатный).

Данный репозиторий создан для выполнения финального задания 4-го модуля. Установив его себе, можно запускать готовые авто тесты, написанные для сайта http://selenium1py.pythonanywhere.com/ (к сожалению в 2026-м году он доступен только с VPN).

## Лицензия
Лицензия пока не определена.<br>
Любой может свободно копировать и использовать данный репозиторий в любых целях.

## Установка
На вашем компьютере должны быть установлены:<br>
* [PyCharm](https://www.jetbrains.com/pycharm/download/)<br>
* [Python](https://www.python.org/downloads/) - на момент написания проекта использовалась версия 3.14.<br>
* Драйвер для вашего браузера ([Chrome Web Driver](https://googlechromelabs.github.io/chrome-for-testing/)) или ([Geckodriver](https://github.com/mozilla/geckodriver/releases)), используйте версию драйвера подходящую под версию браузера.

### Клонирование проекта в PyCharm 
1. В PyCharm перейти "File" -> "Project from  Version Control".
2. В поле "URL" ввести ссылку на данный проект: https://github.com/mstowsky/at_stepik_page_object_model.git
3. В поле "Directory" указать путь до папки, где на вашем компьютере будет храниться проект (можно оставить по умолчанию).
4. Нажать "Clone".
5. Открыть склонированный проект в текущем окне (This Windows) или в новом (New Windows).
6. Если автоматически открылось окно "Creating Virtual Environment", то в поле "Base interpreter" выбрать из списка путь до установленного python.
7. Нажать "ОК".
8. Дождаться создания виртуального окружения и установки зависимостей проекта.
9. PROFIT!

## Запуск тестов
В PyCharm открыть Terminal (ALT+F12), вписывать туда команды:
* Запустить все имеющиеся тесты: `pytest -v -s --tb=line tests`
* Запустить все тесты по странице: `pytest -v -s --tb=line tests\test_login_page.py`
* Запустить все тесты класса (тест-сьюта): `pytest -v -s --tb=line tests\test_login_page.py::TestGuestTests`
* Запустить один определенный тест: `pytest -v -s --tb=line -k test_user_can_add_product_to_basket`<br>

По умолчанию используется браузер Chrome и английский язык сайта. Можно использовать другой браузер и другой язык, для этого добавить ключи `--browser_name` и `--language` соответственно.<br>
Пример: `pytest -v -s --tb=line --browser_name=firefox --language=ru -k test_user_can_add_product_to_basket`