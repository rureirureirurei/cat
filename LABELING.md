### general
Є багато датасетів. Кожний датасет - таблиця. В кожному окремому столбці лежать окремі значення. Наприклад, в перщому столбці може бути імʼя, в другому - фамілія, в третьому - дата народження, тощо.

Що треба робити?
Цей проєкт про визначення “типу” данних за значеннями та назві столбця.

Наприклад -
значення: ```Alice, Bob, John, ...``` з назвою столбця ```PAT_NAMES```- очевидно має тип ```names```

Для того щоб натренувати модель мені потрібно багато даних. То що описано нижче - процес підготовки даних.

Коли тебе запустиш програму - в консолі будуть виводитися різні штуки:
   - ім'я датасета
   - кількість колонок у датасеті
   - перші 7 значень зі стовпчика
   - Назва стовпчика.

Наприклад:
```
filename: First_Health_Camp_Attended.csv
cols: 5

0    506181
1    494977
2    518680
3    509916
4    488006
5    492080
6    521555
Name: Patient_ID, dtype: int64

SKIP
detected types id

0    6560
1    6560
2    6560
3    6560
4    6560
5    6560
6    6560
Name: Health_Camp_ID, dtype: int64)
```

```First_Health_Camp_Attended.csv``` - назва датасету

```5``` - кількість колонок

```506181, 494977, 518680, …``` - значення елементів 

```Patient_ID``` - назва столбця. 

```
SKIP
detected types id
``` 
це значить що программа сама визначила що це тип ```id``` і перейшла до наступного стовбчика.

У відповіді потрібно написати тип, останнього що виведено 

(в цьому випадку це 6560,6560,... з назвою стовбця Health_Camp_ID). 

За назвою зрозуміло що це ```id```. Треба написати ```id``` і натиснути ```enter```

Власне, все.

### a bit bout cats


Всі адекватні можливі типи я написав у файлі ```cats```.
Якщо в ```cats``` написано щось із відсупами - ігноруй слово з двокрапкою. Тобто

```
. . .
temporal:
  date
  time
  datetime
  year
  day
. . . 
```
на temporal забиваеш. валідні типи це: date, time, datetime, year, day

Якщо якогось типу не вистачає, але хотілося б - додай в ```cats``` (просто в кінці допиши) і у відповідь дай новий тип.

### a bit bout types

Якщо підходить кілька типів – пиши їх у відповіді через кому. Наприклад: ```latitude, longitute, eshe-cheto```. Якщо в назві типу два слова - їх писати через дефіс, наприклад: ```phone-number```.

Якщо тип незрозуміло, що це - у відповідь потрібно написати ```?```.

Якщо в датасеті якась лажа - можна написати ```???```. Тоді скрипт сам заповнить все що залишилось для даного датасету та відкриє наступний.

### приколяхі

Якщо для якогось датасету вже були записані типи - в консолі буде щось таке:
  ```
  SKIP
  found labels fileDrugs_unfinished_package.csv
  ```
  тобто для ```fileDrugs_unfinished_package.csv``` вже було записано відповіді

  

Ось ці процентікі(```5%|██████```) значать скільки від усіх датасетів було вже оброблено.

Коли для датасету скінчились колонки і відповіді було записано, в консолі буде щось типу: ```Saved labels ✅```

Якщо для датасету вже були записані типи - наступного разу іх не треба записувати.