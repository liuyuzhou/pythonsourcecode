class WeatherSearch(object):
    def __init__(self, input_daytime):
        self.input_daytime = input_daytime

    def search_visibility(self):
        """
        能见度级别
        :return: visible_leave
        """
        visible_leave = 0
        if self.input_daytime == 'daytime':
            visible_leave = 9
        if self.input_daytime == 'night':
            visible_leave = 3
        return visible_leave

    def search_temperature(self):
        """
        温度
        :return: temperature
        """
        temperature = 0
        if self.input_daytime == 'daytime':
            temperature = 20
        if self.input_daytime == 'night':
            temperature = 16
        return temperature

    def search_wetness(self):
        """
        空气湿度
        :return: wetness
        """
        wetness = 0
        if self.input_daytime == 'daytime':
            wetness = 50
        if self.input_daytime == 'night':
            wetness = 100
        return wetness
