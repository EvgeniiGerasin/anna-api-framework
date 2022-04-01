import allure
import pytest

from framework import Action
from framework import Assert
from framework import Report


@allure.epic('Testing API OpenWather')
class TestWatherAPI:

    @allure.title('Get current wather by lat and lon')
    @pytest.mark.parametrize(
        'geo',
        [
            ['35', '140'],
            ['35', '141'],
            ['35', '143'],
            ['35', '144'],
            ['35', '148'],
        ]
    )
    def test_call_current_weather_data(self, geo):
        method = 'GET'
        lat = geo[0]
        lon = geo[1]
        appid = '43696882c59420349118379491c29716'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        Report.put_description(
            url=url,
            appid=appid,
            lat=lat,
            lon=lon
        )
        session = Action(url)
        got = session.request(
            method=method,
            params={
                'lat': lat,
                'lon': lon,
                'appid': appid,
            }
        )
        want = 200
        with allure.step('Check status code'):
            Assert.equality(
                want, got.status_code, "Want {} but got {}".format(want, got)
            )
