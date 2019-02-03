# Schedule parser


import urllib.request
from bs4 import BeautifulSoup
import schedule_class as SC


URL = 'https://students.bmstu.ru/schedule/62ee7ad2-a264-11e5-8179-005056960017'
week = []


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):

    soup = BeautifulSoup(html, features="html.parser")
    data = soup.find('div', class_ = 'row')
    divs = data.find_all('tbody') 

    counter = 1
    for i in divs:
        # print(i.tr.td.strong.text)

        # On the site schedule have 2 similar versions
        # which plased in the same table

        # We need only 1 wersion, so we take only
        # odd version

        if counter % 2:

            day = i.find_all('tr')
            
            counter1 = 0

            for j in day:

                day_schedule = SC.DaySchedule()

                data_of_day = j.find_all('td')

                if counter1 == 0:

                    day_of_week = j.td.text

        ###----------------------
                    day_schedule.day_of_week = day_of_week + '\n'

                elif counter1 == 1:
                    pass

                else:
                    
                    time_of_lesson = data_of_day[0].text

        ###-----------------------
                    day_schedule.time_of_classes[counter1 - 2] = time_of_lesson + '\n'

                    if 'colspan=' not in str(data_of_day):

                        # Тогда у нас 3 поля td
                        
                        odd_lesson = data_of_day[1].text

                        if odd_lesson == '':
                            odd_lesson = '---'

                        even_lesson = data_of_day[2].text

                        if even_lesson == '':
                            even_lesson = '---'

        ###-----------------------
                        day_schedule.classes[counter1 - 2] = '  (чс) ' + odd_lesson + '\n   (зн) ' + even_lesson + '\n'


                    else:

                        odd_lesson = even_lesson = data_of_day[1].text

        ###-----------------------
                        day_schedule.classes[counter1 - 2] = '  ' + data_of_day[1].text + '\n'

                # print(data_of_day)
                
                print(
                day_schedule.day_of_week,
                day_schedule.time_of_classes[counter1 - 2],
                day_schedule.classes[counter1 - 2],
                )

                week.append(day_schedule)
                counter1 += 1

            print('********************************')
            week.append(day_of_week)

        counter +=1



def main():
    html = get_html(URL)
    parse(html)
    

    # for one_day in week:
    #      print(one_day.schedule)
    #      print()


if __name__ == '__main__':
    main()
