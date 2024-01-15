# kilovolts
Открытый, быстрый и простой PCB эмулятор на Python

![Static Badge](https://img.shields.io/badge/OkulusDev-kilovolts-kilovolts)
![GitHub top language](https://img.shields.io/github/languages/top/OkulusDev/kilovolts)
![GitHub](https://img.shields.io/github/license/OkulusDev/kilovolts)
![GitHub Repo stars](https://img.shields.io/github/stars/OkulusDev/kilovolts)
![GitHub issues](https://img.shields.io/github/issues/OkulusDev/kilovolts)

## About
В нашем эмуляторе PCB "Kilovolts" есть класс компонента и линейного компонента, они являются родительскими классами других компонентов (резистор линейный компонент, транзистор обычный компонент). Существует система связей при помощи проводов. Пока доступно только взаимодействие из python кода, в будущем будет GUI интерфейс.

## Документация
Пользовательскую документацию можно получить по [этой ссылке](./docs/ru/index.md).

[Релизы программы]: https://github.com/OkulusDev/kilovolts/releases

## Поддержка
Если у вас возникли сложности или вопросы по использованию пакета, создайте 
[issue](https://github.com/OkulusDev/Oxygen/issues/new/choose) в данном репозитории или напишите на электронную почту <bro.alexeev@inbox.com>.

## Установка
У вас на ПК должен быть установлен python>=~3.8

```bash
git clone https://github.com/OkulusDev/kilovolts		# клонирование репозитория
cd kilovolts
python3 kilovolts.py 									# запуск
```

## Copyright
Copyright (C) 2024  Alexeev Bronislav "Okulus" or "Hex"

An open, fast and simple python PCB board emulator
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see [GNU Licenses](https://www.gnu.org/licenses/).
    
## Описание коммитов
| Название | Описание                                                        |
|----------|-----------------------------------------------------------------|
| build	   | Сборка проекта или изменения внешних зависимостей               |
| sec      | Безопасность, уязвимости                                        |
| ci       | Настройка CI и работа со скриптами                              |
| docs	   | Обновление документации                                         |
| feat	   | Добавление нового функционала                                   |
| fix	   | Исправление ошибок                                              |
| perf	   | Изменения направленные на улучшение производительности          |
| refactor | Правки кода без исправления ошибок или добавления новых функций |
| revert   | Откат на предыдущие коммиты                                     |
| style	   | Правки по кодстайлу (табы, отступы, точки, запятые и т.д.)      |
| test	   | Добавление тестов                                               |

