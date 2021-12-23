import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    logging.warning("hello world")
     #######################################
    print("hello world")
    logging.warning("prova-deploy")
 
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    return None