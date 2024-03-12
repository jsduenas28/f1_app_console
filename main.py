import asyncio
import os
from functions import race_schedule, standings, templates
from pyfiglet import Figlet
from termcolor import colored

async def main():
    while True:
        custom = Figlet(font='standard')
        os.system('cls')
        print(colored(custom.renderText('F1 App'), 'red'))
        print('\n¿Qué quieres hacer?')
        print('1. Buscar una carrera específica')
        print('2. Siguiente carrera')
        print('3. Carrera Anterior')
        print('4. Campeonato de Pilotos')
        print('5. Campeonato de Constructores')
        print('6. Informacion de la app')
        print('7. Salir')
        opcion = input('Escribe tu opción: ')
        
        while opcion not in {'1', '2', '3', '4', '5', '6', '7'}:
            print('Opción no válida. Por favor, elige una opción válida.')
            opcion = input('Escribe tu opción: ')

        if opcion == '1':
            await race_schedule.specific_race()
            input('\nPresiona Enter para volver al menú principal...')
        elif opcion == '2':
            await race_schedule.next_race()
            input('\nPresiona Enter para volver al menú principal...')
        elif opcion == '3':
            await race_schedule.last_race()
            input('\nPresiona Enter para volver al menú principal...')
        elif opcion == '4':
            await standings.driverStanding()
            input('\nPresiona Enter para volver al menú principal...')
        elif opcion == '5':
            await standings.constructoStanding()
            input('\nPresiona Enter para volver al menú principal...')
        elif opcion == '6':
            templates.info_app()
            input('\nPresiona Enter para volver al menú principal...')
        elif opcion == '7':
            templates.despedida()
            break
        
if __name__ == '__main__':
    asyncio.run(main())