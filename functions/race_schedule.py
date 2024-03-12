from aiohttp import ClientSession
import xmltodict, json
import os
from pyfiglet import Figlet
from termcolor import colored

async def get_race(session, url:str, keys: list):
    async with session.get(url) as response:
        data = await response.text()
        o = xmltodict.parse(data)
        race = json.dumps(o, indent=2)
        race_data = json.loads(race)

        result = race_data
        for key in keys:
            result = result[key]
        
        return result

async def next_race():
    """
    Muestra la siguiente carrera o la carrera anterior
    
    la condicional que esta al final sirve para saber si la carrera tiene Practica 3 o Carrera Sprint
    """
    async with ClientSession() as session:
        custom = Figlet(font='standard')
        url = "https://ergast.com/api/f1/current/next"
        keys = ['MRData', 'RaceTable', 'Race']
        race = await get_race(session=session, url=url, keys=keys)
        os.system('cls')
        print(colored(custom.renderText(race['RaceName']), 'red'))
        print(race['Circuit']['Location']['Locality'] + ' - '  + race['Circuit']['Location']['Country'])
        print('Temporada: ' + race['@season'] + ' - Ronda: ' + race['@round'])
        print('Circuito: ' + race['Circuit']['CircuitName'])
        print('-----------------------------------------------')
        print('Carrera: ' + race['Date'] + ' - ' + race['Time'])
        print('Qualy: ' + race['Qualifying']['Date'] + ' - ' + race['Qualifying']['Time'])
        print('Practica Libre 1: ' + race['FirstPractice']['Date'] + ' - ' + race['FirstPractice']['Time'])
        print('Practica Libre 2: ' + race['SecondPractice']['Date'] + ' - ' + race['SecondPractice']['Time'])
        
        if 'ThirdPractice' in race:
            print('Practica Libre 3: ' + race['ThirdPractice']['Date'] + ' - ' + race['ThirdPractice']['Time'])
        elif 'Sprint' in race:
            print('Carrera Sprint: ' + race['Sprint']['Date'] + ' - ' + race['Sprint']['Time'])

async def last_race():
    """
    Optiene la carrera anterior ademas de mostrar los resultados de esa carrera
    """
    async with ClientSession() as session:
        custom = Figlet(font='standard')
        url = "https://ergast.com/api/f1/current/last/results"
        keys = ['MRData', 'RaceTable', 'Race']
        race = await get_race(session=session, url=url, keys=keys)
        os.system('cls')
        print(colored(custom.renderText(race['RaceName']), 'red'))
        print(race['Circuit']['Location']['Locality'] + ' - '  + race['Circuit']['Location']['Country'])
        print('Temporada: ' + race['@season'] + ' - Ronda: ' + race['@round'])
        print('Circuito: ' + race['Circuit']['CircuitName'])
        print('Carrera: ' + race['Date'] + ' - ' + race['Time'])
        print('-----------------------------------------------\n')
        
        print('Resultados de carrera\n')
        
        print(colored("{:<8} {:<8} {:<20} {:<20} {:<8} {:<8} {:<15} {:<10} {:<8}".format("POS", "No", "Driver", "Constructor", "Laps", "Grid", "Time", "Status", "Points"), 'red'))
        results = race['ResultsList']
        for key, value in results.items():
            if isinstance(value, list):
                for result in value:
                    drivername = result['Driver']["GivenName"] + ' ' + result['Driver']["FamilyName"]
                    print("{:<8} {:<8} {:<20} {:<20} {:<8} {:<8} {:<15} {:<10} {:<8}".format(result["@positionText"], result["@number"], drivername, result['Constructor']['Name'], result['Laps'], result['Grid'], result['Time']['#text'] if 'Time' in result else '', result['Status']['#text'], result["@points"]))

async def specific_race():
    """
    Busca una carrera especifica
    
    var: round -> optione el numero de ronda espeficica para buscar la carrera y lo coloca en la url
    
    la condicional que esta al final sirve para saber si la carrera tiene Practica 3 o Carrera Sprint
    """
    async with ClientSession() as session:
        custom = Figlet(font='standard')
        os.system('cls')
        round = input('Escribe la ronda (1 - 24): ')
        url = f"https://ergast.com/api/f1/current/{round}"
        keys = ['MRData', 'RaceTable', 'Race']
        race = await get_race(session=session, url=url, keys=keys)
        os.system('cls')
        print(colored(custom.renderText(race['RaceName']), 'red'))
        print(race['Circuit']['Location']['Locality'] + ' - '  + race['Circuit']['Location']['Country'])
        print('Temporada: ' + race['@season'] + ' - Ronda: ' + race['@round'])
        print('Circuito: ' + race['Circuit']['CircuitName'])
        print('-----------------------------------------------')
        print('Carrera: ' + race['Date'] + ' - ' + race['Time'])
        print('Qualy: ' + race['Qualifying']['Date'] + ' - ' + race['Qualifying']['Time'])
        print('Practica Libre 1: ' + race['FirstPractice']['Date'] + ' - ' + race['FirstPractice']['Time'])
        print('Practica Libre 2: ' + race['SecondPractice']['Date'] + ' - ' + race['SecondPractice']['Time'])
        
        if 'ThirdPractice' in race:
            print('Practica Libre 3: ' + race['ThirdPractice']['Date'] + ' - ' + race['ThirdPractice']['Time'])
        elif 'Sprint' in race:
            print('Carrera Sprint: ' + race['Sprint']['Date'] + ' - ' + race['Sprint']['Time'])