import json
import numpy
from typing import List,Dict
from useRequest import useRequest
from xml.dom.minidom import parseString
from loggers import logger,error_logger
from map import generateMap


type Record = list[List[str,str]]
type Data = list[Dict[str,str]]

def run_from_local(filename):
    print("=" * 80)
    with open(filename,mode='r') as f:
        logger.info(f"Running from local file")
        logger.info(f"Reading records from {filename} file")
        records = json.load(f)
        generateMap(records)


def run(filename):
    try:
         # request the xml file from the server
        response = useRequest("https://volcanoes.usgs.gov/hans-public/api/map/getVhpStatus","GET")
        records = transform_xmlToDict(response)
      
        # update directory json file
        update(filename,records)
        generateMap(records)

    except Exception as e:
        error_logger.error("Unable to generate map using server records")
        error_logger.error(e)
        return False
    
    return True


def update(filename,records):

    with open(filename,mode='w') as f:
        logger.info(f"updating {filename} file...")
        f.write(json.dumps(records,indent=4))
        logger.info("File updated...")


def create_dictList(data:Record) -> Data:
    """
    creates a dictionary list from an array of arrays

    Args:
        data (Record): the records that needs to be transform

    Returns:
        Data: a list of dictionaries
    """
    return [dict(info) for info in data]

def custom_sort(data:Record) -> Record:
    """
      sort an array of arrays by using the inner array first index

    Args:
        data (Record): the record that needs to be sorted

    Returns:
        Record: a sorted record
    """

    return [sorted(info,key=lambda x : x[0]) for info in data]
   
def transform_xmlToDict(xml_text,sorted=True):
    """Transform the given xml responsse into a list of dictionary objects"""
    logger.info("converting xml to dictionary")
    dom = parseString(xml_text)

    # get the marker tags from the xml dom
    markers = dom.getElementsByTagName('marker')

    # creates a list of dom tags from the markers tag of the page
    element_list = [element.attributes.items() for element in markers]

    # returns an array of arrays
    output = numpy.array(element_list)

    if sorted:
       output = custom_sort(output)

    return create_dictList(output)
 