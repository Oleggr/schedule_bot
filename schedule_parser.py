# Schedule parser

import datetime

import urllib.request
from bs4 import BeautifulSoup
import schedule_class as SC


# ИУ3-53 - перестал работать
# URL = 'https://students.bmstu.ru/schedule/62ee7ad2-a264-11e5-8179-005056960017'


# ИУ3-63
# URL = 'https://students.bmstu.ru/schedule/62ee7b7c-a264-11e5-a475-005056960017'

# ИУ7-63
URL = 'https://students.bmstu.ru/schedule/62eca0d6-a264-11e5-84ad-005056960017'

week = []
DATA_FORMAT = '%Y'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):

    soup = BeautifulSoup(html, features="html.parser")

    # Before we'll find schedule
    # we must find group name

    header = soup.find('div', class_ = "page-header")
    # print(header)
    name_of_group = header.find('h1').text[11:]
    
    b = datetime.datetime.now().strftime(DATA_FORMAT)

    filename = name_of_group + '.' + b + '.txt'

    with open (filename, 'w') as f:
        
        # Find schedule

        data = soup.find('div', class_ = 'row')
        # print(data)
        divs = data.find_all('tbody') 

        # Counter need because of strange structure of schedule

        counter = 1

        for i in divs:

            # On the site schedule have 2 similar versions
            # which plased in the same table

            # We need only 1 wersion, so we take only
            # odd version

            if not counter % 2:

                day = i.find_all('tr')
                
                counter1 = 0

                for j in day:

                    # day_schedule = SC.DaySchedule()

                    data_of_day = j.find_all('td')

                    if counter1 == 0:

                        day_of_week = j.td.text

                        f.write(day_of_week + '\n')

            ###----------------------
                        # day_schedule.get_new_val_for_day_of_week(day_of_week + '\n')

                    elif counter1 == 1:
                        pass

                    else:
                        
                        time_of_lesson = data_of_day[0].text

                        f.write(time_of_lesson + '\n')

            ###-----------------------
                        # day_schedule.time_of_classes[counter1 - 2] = time_of_lesson + '\n'

                        if 'colspan=' not in str(data_of_day):

                            # Тогда у нас 3 поля td
                            
                            odd_lesson = data_of_day[1].text

                            if odd_lesson == '':
                                odd_lesson = '---'

                            even_lesson = data_of_day[2].text

                            if even_lesson == '':
                                even_lesson = '---'

                            f.write(
                                    '(чс) ' + odd_lesson + '\n'
                                    + '(зн) '+ even_lesson+ '\n\n'
                                    )

            ###-----------------------
                            # day_schedule.classes[counter1 - 2] = '  (чс) ' + odd_lesson + '\n   (зн) ' + even_lesson + '\n'


                        else:

                            odd_lesson = even_lesson = data_of_day[1].text

                            f.write(even_lesson+ '\n\n')

            ###-----------------------
                            # day_schedule.classes[counter1 - 2] = '  ' + data_of_day[1].text + '\n'

                    # print(data_of_day)
                    
                    # print(
                    # day_schedule.return_day_of_week(),
                    # day_schedule.time_of_classes[counter1 - 2],
                    # day_schedule.classes[counter1 - 2],
                    # )

                    # week.append(day_schedule)

                    counter1 += 1

                f.write('********************************\n')

            counter +=1



def main():
    html = get_html(URL)
    parse(html)
    

    # for one_day in week:
    #      print(one_day.schedule)
    #      print()


if __name__ == '__main__':
    main()
