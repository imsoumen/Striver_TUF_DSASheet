class Solution:
    def whichWeekDay(self, day):
        if day > 7 or day < 1:
            print('Invalid')
        else:
            mapp = {
                1 : 'Monday',
                2 : 'Tuesday',
                3 : 'Wednesday',
                4 : 'Thursday',
                5 : 'Friday',
                6 : 'Saturday',
                7 : 'Sunday'
            }
            print(mapp[day])

