import time


class LogIt:

    def __init__(self, file='log.txt', levels=None):
        self.levels = levels
        self.have_levels = False
        self.session_name = ''
        self.data = ''
        self.date = ''
        
        self.file = file
        self.text_format = ''
        self.date_format = ''

        if self.levels != None:
            self.have_levels = True


    def Format(self, text_format='[{session_name}] {date} !{level}! -> {message}', data=None, date_format='%Y-%m-%d %H:%M:%S'):
        self.text_format = text_format
        self.date_format = date_format
        if data == None:
            self.data = {'session_name': self.session_name, 'date': time.strftime(self.date_format, time.asctime()), 'level': 'INFO', 'message': 'Hello world!'}
        else:
            self.data = data
            try:
                self.data['date_format']
            except KeyError:
                self.data['date_format'] = '%Y-%m-%d %H:%M:%S'
                self.data['message'] = ''
                self.data['level'] = ''

    def Logging(self, message='Hello world!', level='INFO', data=''):
        self.data['message'] = message
        if self.have_levels:
            try:
                self.levels[level]
            except KeyError:
                print('Key Error. The specified level was not found.')
            else:
                self.data['level'] = self.levels[level]
        else:
            self.data['level'] = level
        
        self.data['date'] = time.strftime(self.date_format, time.gmtime())
        with open(self.file, 'a') as f:
            f.write(self.text_format.format(**self.data)+'\n')


# сделать кастомный формат даты