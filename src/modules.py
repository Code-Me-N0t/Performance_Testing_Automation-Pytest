import time, json, pytest, requests, pyautogui, logging, os, psutil
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from colorama import Fore, init

logging.basicConfig(level=logging.CRITICAL + 1)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def load_json(filename):
    with open(filename) as json_file:
        json_data = json_file.read()
        return json.loads(json_data)

creds = load_json('creds.json')

init(autoreset=True)