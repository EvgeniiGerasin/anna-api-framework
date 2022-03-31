import requests
import allure

from tools.actions import Action


class TestWatherAPI:

    @allure.title('Get current wather')
    def test_call_current_weather_data(self):

        session = Action('https://api.openweathermap.org/data/2.5/weather')
        got = session.request(
            type='POST',
            params={
                'lat': '35',
                'lon': '139',
                'appid': '43696882c59420349118379491c29716',
            }
        )
        want = 200
        with allure.step('Check status request'):
            assert got.status_code == want, got.text
