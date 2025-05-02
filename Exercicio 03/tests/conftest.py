# arquivo conftest.py
import os
from pytest import fixture
from selenium import webdriver

@fixture
def form_cliente():
    chrome = webdriver.Chrome()
    pasta = os.path.dirname(os.path.realpath(__file__))
    local_path = f'file://{pasta}/../app/template/'
    chrome.get(f'{local_path}cliente.html')
    yield chrome
    chrome.close()