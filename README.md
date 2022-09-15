# Open-source проект VOZDOOH.info
## https://vozdooh.info/


![telegram](https://img.shields.io/badge/Telegram-arud3nko-informational?style=for-the-badge&logo=appveyor)
![issues](https://img.shields.io/github/issues/arud3nko/python-ML-airpollution?label=ISSUES&style=for-the-badge)
![serverstatus](https://img.shields.io/website?down_message=OFFLINE&label=SERVER&style=for-the-badge&up_message=Running&url=http%3A%2F%2Funiver.icu)


***

## Ход разработки
· Получены токены API сервисов Яндекс.Погода, nebo.live

· Спроектирована MySQL база данных, размещена на удаленном сервере

· Идёт наполнение базы данных 

· На основе полученных данных сгенерирован график, показывающий зависимость уровня загрязнения от погодных условий

· Создан landing-page на Flask



![site](https://i.ibb.co/71JnpkP/2022-03-29-11-11-16-PM.png)

· Создан макет Telegram-бота в Figma: https://www.figma.com/file/YUI2ipUfK9KhMZ3sNFBU5v/Prototyping-in-Figma

· Обучена нейронная сеть для прогнозирования качества воздуха

· (**15.09.22**) Полный рефактор кода с другим подходом к прогнозированию

· (**15.09.22**) Полный редизайн веб-страницы сервиса

![new-site](https://sun9-west.userapi.com/sun9-4/s/v1/ig2/r-A12hKD7XTZdQNszlysGk4XJgXml8SM79w6BkCHkLaqAeAj5UzraxCjuT6jiMVMw2voU1rxqyM57gQgCbXnn6ZF.jpg?size=2560x1403&quality=96&type=album)

***

## Задачи
1) ~~Организовать парсинг данных одного из погодных сервисов~~
2) ~~Организовать сбор показателей уровня загрязнения воздуха, используя сервис nebo.live~~
3) ~~Создать ML-модель, вычисляющую зависимость уровня загрязнения воздуха от погодных условий~~
4) ~~Проработать и организовать методы оповещения: web-сервис на Flask и/или Telegram-бот~~
5) (**15.09.22**) Рефактор модуля DataCapture
6) (**15.09.22**) Корректировка верстки под мобильную версию сайта
7) (**15.09.22**) Полный переход на API от tomorrow.io

***

## Цель
~~Создать сервис, заранее рассчитывающий уровень загрязнения, в зависимости от погодных условий.~~

Выполнено ✅
