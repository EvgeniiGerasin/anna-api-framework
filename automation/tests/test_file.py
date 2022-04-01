import pytest

from framework import Action
from framework import Assert
from framework import Report


@Report.epic('Testing API OpenWather')
@Report.feature('Testing requests with different methods')
@Report.link('https://openweathermap.org/', 'OpenWeatherMap')
@Report.testcase('https://openweathermap.org/current', 'How to make an API call')
class TestWatherAPI:

    @Report.title('Get current wather by lat and lon and GET method')
    @Report.severity('CRITICAL')
    @pytest.mark.parametrize(
        'geo',
        [
            ['35', '140'],
            ['35', '141'],
        ]
    )
    def test_call_current_weather_data(self, geo):
        method = 'GET'
        lat = geo[0]
        lon = geo[1]
        appid = '43696882c59420349118379491c29716'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        Report.description(
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
        with Report.step('Check status code'):
            Assert.equality(
                want, got.status_code, "Want {} but got {}".format(want, got)
            )

    @Report.title('Get current wather by lat and lon and POST method')
    @Report.severity('NORMAL')
    @pytest.mark.parametrize(
        'geo',
        [
            ['35', '140'],
            ['35', '141'],
        ]
    )
    def test_call_current_weather_data_POST(self, geo):
        method = 'POST'
        lat = geo[0]
        lon = geo[1]
        appid = '43696882c59420349118379491c29716'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        Report.description(
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
        with Report.step('Check status code'):
            Assert.equality(
                want, got.status_code, "Want {} but got {}".format(want, got)
            )
