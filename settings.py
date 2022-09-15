import configparser
import os.path

''' Об использовании на сервере
    OS: Debian 10, стек LAMP
    /home/vozdooh/......
Для доступа к верхним директориям из любой рут-директории: 
    import sys
    sys.path.append("/home/vozdooh")
Для доступа к верхним директориям из скриптов:
    import sys
    sys.path.append("..")
Задача в crontab на каждые 30мин:
    */30 * * * * python3 /home/vozdooh/DataCapture/cdata.py

'''

# --- use True if running on server ---
SERVER_USE = False


def get_config():
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
    config = configparser.ConfigParser()
    config.read(directory+'/conf.ini')
    default_config = config['DEFAULT']

    class Config:
        WEATHER_API_KEY = default_config['WEATHER_API_KEY']
        NEBO_API_CODE = default_config['NEBO_API_CODE']
        NEBO_API_TOKEN = default_config['NEBO_API_TOKEN']
        TOMORROW_API_TOKEN = default_config['TOMORROW_API_TOKEN']
        HOST = default_config['HOST']
        USER = default_config['USER']
        PASSWORD = default_config['PASSWORD']
        DATABASE = default_config['DATABASE']

        if SERVER_USE:
            GLOBAL_PATH = config['SERVER']['GLOBAL_PATH']
        else:
            GLOBAL_PATH = config['LOCAL']['GLOBAL_PATH']

    return Config


def main():
    pass


if __name__ == '__main__':
    main()
