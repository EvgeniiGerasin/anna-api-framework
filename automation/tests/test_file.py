import requests
import allure

from tools.actions import Action


class TestWatherAPI:

    @allure.title('Get current wather')
    def test_call_current_weather_data(self):
        
        # r = requests.get(
        #     'https://api.openweathermap.org/data/2.5/weather',
        #     params={
        #         'lat': '35',
        #         'lon': '139',
        #         'appid': '43696882c59420349118379491c29716',
        #     }
        # )

        session = Action('https://api.openweathermap.org/data/2.5/weather')
        got = session.get(
            params={
                'lat': '35',
                'lon': '139',
                'appid': '43696882c59420349118379491c29716',
            }
        )
        assert got.status_code == 200, got.text
