import sys
import time
import logging
import threading
import RPi.GPIO as GPIO
import requests
import smtplib
import json
import builtins
from time import localtime, strftime

from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read("config.ini")

def welcome():
    try:
        print(5)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        pass