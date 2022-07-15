from anna import Action
from anna import Report
from anna import Assert


@Report.epic('Test OpenWeather')
@Report.link('https://openweathermap.org/', 'OpenWeatherMap')
@Report.testcase('https://openweathermap.org/api', 'OpenWeatherMap API')
class TestOpenWeather:

    @Report.feature('Simple requests')
    @Report.title('Current weather by lat and lon')
    def test_current_weather_by_lat_lon(self, user_params):
        lat, lon = '55.751244', '37.618423'
        api_id = user_params
        url = 'http://api.openweathermap.org/data/2.5/weather'
        Report.description(url=url, api_id='*****', lat=lat, lon=lon)
        action = Action()
        want = 200
        got = action.request('GET', url=url, params={'lat': lat, 'lon': lon, 'appid': api_id}).status_code
        with Report.step('Check status code'):
            Assert.compare(want, '=', got, 'Status code != {}'.format(want))
