class DaySchedule():
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

    pairity = '' # odd or even week

    day_of_week = ''

    def get_new_val_for_time_of_classes(self, val):
        self.time_of_classes = val

    def get_new_val_for_classes(self, val):
        self.classes = val

    def get_new_val_for_day_of_week(self, val):
        print('*+-=-+*')
        print(val)
        print(self.day_of_week)
        self.day_of_week = val

    def return_time_of_classes(self):
        return self.time_of_classes

    def return_classes(self):
        return self.classes

    def return_day_of_week(self):
        return self.day_of_week

    def get_schedule(self):
        '''
        Get schedule function
        '''

        schedule = {
                    'day': self.day_of_week,
                    'pairity': self.pairity,
                    'lessons': [[[self.time_of_classes[0]], self.classes[0]],
                                [self.time_of_classes[1], self.classes[1]],
                                [self.time_of_classes[2], self.classes[2]],
                                [self.time_of_classes[3], self.classes[3]],
                                [self.time_of_classes[4], self.classes[4]],
                                [self.time_of_classes[5], self.classes[5]],
                                [self.time_of_classes[6], self.classes[6]]]
                    }
         
        return self.schedule                   
