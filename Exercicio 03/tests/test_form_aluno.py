# arquivo test_form_cliente.py
import time
from selenium.webdriver.common.by import By

def test_localizar_campo_nome(form_cliente):
    campo_nome = form_cliente.find_element(By.NAME, 'nome_cliente')
    assert campo_nome.tag_name == 'input'
    assert campo_nome.get_attribute('placeholder') == 'nome do cliente'
    assert campo_nome.get_attribute('type') == 'text'
    time.sleep(8)

def test_localizar_campo_email(form_cliente):
    campo_email = form_cliente.find_element(By.NAME, 'email')
    assert campo_email.tag_name == 'input'
    assert campo_email.get_attribute('placeholder') == 'e-mail'
    assert campo_email.get_attribute('type') == 'email'
    time.sleep(8)

def test_localizar_campo_login(form_cliente):
    campo_login = form_cliente.find_element(By.NAME, 'login')
    assert campo_login.tag_name == 'input'
    assert campo_login.get_attribute('type') == 'submit'
    assert campo_login.get_attribute('value') == 'Login'
    time.sleep(8)

def test_localizar_form_cliente(form_cliente):
    form_cliente = form_cliente.find_element(By.ID, 'FormCliente')
    assert form_cliente.tag_name == 'form'
    time.sleep(8)

def test_verificar_titulo_do_form(form_cliente):
    assert form_cliente.title == 'Cadastro de cliente'
    time.sleep(8)

