from weather_search import WeatherSearch


class OutAdvice(WeatherSearch):
    def __init__(self, input_daytime):
        WeatherSearch.__init__(self, input_daytime)

    def advice_vehicles(self):
        """
        建议交通工具
        :return:
        """
        vehicles = ''
        if self.input_daytime == 'daytime':
            vehicles = 'bike'
        if self.input_daytime == 'night':
            vehicles = 'taxi'
        return vehicles

    def out_advice(self):
        """
        出行建议
        :return:
        """
        v_leave = self.search_visibility()
        wetness = self.search_wetness()
        vehicles = self.advice_vehicles()
        if v_leave == 9:
            print(f'现在能见度为{v_leave},空气湿度为{wetness}，适合使用{vehicles}出行。')
        elif v_leave == 3:
            print(f'现在能见度为{v_leave},空气湿度为{wetness}，适合使用{vehicles}出行。')
        else:
            print('目前天气情况比较复杂，请您谨慎出行。')


# 白天出行建议
check = OutAdvice('daytime')
check.out_advice()
# 夜晚出行建议
check = OutAdvice('night')
check.out_advice()
# 下雪天出行建议
check = OutAdvice('snow')
check.out_advice()
