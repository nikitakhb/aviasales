# Aviasales Case
Case For Aviasales

Запуск кейса
```
docker-compose -f docker-compose.dev.yml up --build
```
Кейс запустится на 80 порту.
Имеется swagger.
```
http://0.0.0.0/
```
Запуск тестов
```
pipenv install
cd case && pytest
```

