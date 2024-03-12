from aiohttp import ClientSession
import xmltodict, json
import os
from pyfiglet import Figlet
from termcolor import colored

async def get_standings(session, url:str, keys:list):
    async with session.get(url) as response:
        data = await response.text()
        a = xmltodict.parse(data)
        driverStanding = json.dumps(a, indent=2)
        driverStanding_data = json.loads(driverStanding)
        
        result = driverStanding_data
        for key in keys:
            result = result[key]
        
        return result

async def driverStanding():
    """
    Muestre la tabla del campeonato de pilotos
    """
    async with ClientSession() as session:
        custom = Figlet(font='standard')
        url = "https://ergast.com/api/f1/current/driverStandings"
        keys = ['MRData', 'StandingsTable', 'StandingsList']
        driver = await get_standings(session=session, url=url, keys=keys)
        os.system('cls')
        print(colored(custom.renderText("Campeonato de Pilotos " + driver['@season'] + '\n'), 'red'))
        
        print(colored("{:<8} {:<20} {:<20} {:<8} {:<8}".format('POS', 'Driver', 'Constructor', 'Points', 'Wins'), 'red'))
        
        results = driver
        for key, value in results.items():
            if isinstance(value, list):
                for result in value:
                    driverName = result['Driver']['GivenName'] + ' ' + result['Driver']['FamilyName']
                    print("{:<8} {:<20} {:<20} {:<8} {:<8}".format(result['@position'], driverName, result['Constructor']['Name'], result['@points'], result['@wins']))

async def constructoStanding():
    """
    Muestra la tabla del campeonato de constructores
    """
    async with ClientSession() as session:
        custom = Figlet(font='standard')
        url = "https://ergast.com/api/f1/current/constructorStandings"
        keys = ['MRData', 'StandingsTable', 'StandingsList']
        constructor = await get_standings(session=session, url=url, keys=keys)
        
        os.system('cls')
        print(colored(custom.renderText('Campeonato de Constructores ' + constructor['@season'] + '\n'), 'red'))
        
        print(colored("{:<8} {:<20} {:<20} {:<8} {:<8}".format('POS', 'Constructor', 'Nationality', 'Points', 'Wins'), 'red'))

        results = constructor
        for key, value in results.items():
            if isinstance(value, list):
                for result in value:
                    print("{:<8} {:<20} {:<20} {:<8} {:<8}".format(result['@position'], result['Constructor']['Name'], result['Constructor']['Nationality'], result['@points'], result['@wins']))