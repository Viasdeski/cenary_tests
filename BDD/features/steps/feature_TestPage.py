from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("que esteja na página de teste")
def acessar_pagina_teste(context):
    context.web.get("your-test-page-url")

@when("clico no botão 'Clique Me'")
def clicar_botao(context):
    botao = context.web.find_element(By.CSS_SELECTOR, "div.centered #button")
    botao.click()

@then("retorna que o botão foi clicado")
def verificar_botao_clicado(context):
    botao = context.web.find_element(By.CSS_SELECTOR, "div.centered #button")
    assert botao.get_attribute("value") == "Botão clicado"
