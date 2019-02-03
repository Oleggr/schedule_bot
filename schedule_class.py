class DaySchedule:
    '''
    Class of schedule

    Saves time, class, cabinet etc.
    '''

    time_of_classes = ['', '', '', '', '', '', ''] # 8.30 - ...

    no_lesson = ' - '

    classes = [ no_lesson,
                no_lesson,
                no_lesson,
                no_lesson,
                no_lesson,
                no_lesson,
                no_lesson ]

    pairity = '' # чс/зн

    day_of_week = ''

    schedule = {
                'day': day_of_week,
                'pairity': pairity,
                'lessons': [[[time_of_classes[0]], classes[0]],
                            [time_of_classes[1], classes[1]],
                            [time_of_classes[2], classes[2]],
                            [time_of_classes[3], classes[3]],
                            [time_of_classes[4], classes[4]],
                            [time_of_classes[5], classes[5]],
                            [time_of_classes[6], classes[6]]]
                }
                            
