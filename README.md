# Проект в рамках дисциплины ВВПД СФУ. 
## Выполняется: София Рус, Егор Удалов

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

***

## Задачи
1) Организовать парсинг данных одного из погодных сервисов
2) Организовать сбор показателей уровня загрязнения воздуха, используя сервис nebo.live
3) Создать ML-модель, вычисляющую зависимость уровня загрязнения воздуха от погодных условий
4) Проработать и организовать методы оповещения: web-сервис на Flask и/или Telegram-бот

***

## Цель
Создать сервис, заранее рассчитывающий уровень загрязнения, в зависимости от погодных условий.

![Иллюстрация к проекту](https://sun9-73.userapi.com/impg/hXUcAJhPO8z6qYBaD6oV-yEZbkvdeRYAQH9epg/u6WFvY7DbzI.jpg?size=1712x1074&quality=96&sign=ea86c5df1e4429034bd6c002a806c863&type=album)


*** 
## Источники:
Nebo.live API: https://nebo.live/docs/v2/index.html
