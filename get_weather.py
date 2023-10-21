# import requests
import requests 
# api key for information from site
api_key = '0a46fc5654b6fdd60e1458adca220281'
# Enter a city  
city = input('Enter your city:')
# link from   which  we take information by api key 
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
# get information from link
response = requests.get(url)
#  check if we can enter by the link
if response.status_code == 200:
    # write information we got in dicitionary
    data = response.json()
    # get the main information
    main_data = data["main"]
    # round the number of the temperature and change it into Celsium degree
    temperature = round(main_data["temp"] - 273.15)
    # get the data we need
    humidity = main_data["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    # print information
    print(f"temperature = {temperature} degree")
    print(f"humidity = {humidity}")
    print(f"Weather description =  {description}")
    print(f"wind speed = {wind_speed}")
    
else:
    # city not found 
    print('There is no city like this')

