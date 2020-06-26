import scrapper


DICT_PAPER_VALUE = 'C_p'


class Paper():

    def __init__(self, paper_id: str):
        if paper_id.isnumeric():
            self._id = paper_id
        else:
            self._id = '11111026'  # S&P 500

        self._points, self._name = scrapper.fetch_paper_data(self._id)

    def get_daily_precetage_change(self):
        val_today = self._points[0].get(DICT_PAPER_VALUE)
        val_yesterday = self._points[1].get(DICT_PAPER_VALUE)

        return round(100 - ((val_today / val_yesterday) * 100), 6)

    def get_daily_rate(self):
        daily_value = self._points[0].get(DICT_PAPER_VALUE)

        return daily_value

    def update_points_data(self):
        self._points = scrapper.fetch_paper_data(self.id)[0]

    def __str__(self):
        return self._id + ' - ' + self._name

    def __repr__(self):
        return f'Paper({self._id}, {self._name})'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name=''):
        if name.isprintable() and name.isalpha():
            self._name = name
        else:
            raise Exception("The paper's name must be valid letters")

    @property
    def id(self):
        return self._id

    @property
    def points(self):
        return self._points