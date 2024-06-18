"""
This application generates an interactive Map of Active Volcanoes  around the glove.
Only highly elevated volcanoes will appear. 
"""
__version__=1.0
__author__="Miguel Ortiz"

from loggers import logger,error_logger
from utils import run,run_from_local



def main():
    logger.info("Program started...")
    volcanoes_file = "volcanoes.json"
    try:
        success = run(volcanoes_file)
        if not success:
            run_from_local(volcanoes_file)
    
    except Exception as e:
        error_logger.error("Fatal Error: Unable to run application")
        error_logger.error(e)



if __name__ == '__main__':
    main()
    