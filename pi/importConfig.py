import configparser

def ImportConfig(configfile):
    config=configparser.ConfigParser()
    config.read(configfile)
    server=config['Server']['serverURL']
    start=config['Start']
    finish=config['Finish']
    return server,start,finish