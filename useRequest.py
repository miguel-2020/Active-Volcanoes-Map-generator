from urllib import request
from loggers import logger
def useRequest(url,method)-> str:
    logger.info("Requesting updated records from the server...")
    """makes an HTTP request

    Args:
        url (str): the source url
        method (str): the method for the request
     

    Returns:
        str: returns an xml file as text
    """

    req = request.Request(url=url,method=method)
    req.add_header("Accept", "application/xml")

    with request.urlopen(req) as xml_response:
        if xml_response.status == 200:
            logger.info("Records successfully loaded")
            return xml_response.read().decode('UTF-8')
        else:
            raise Exception("HTTP response error: Unable to retrieve records from server")
