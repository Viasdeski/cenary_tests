from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.uol.com.br/"

@given("que esteja na tela inicial")
def acessar_site(context):
    context.web.get(base_url)

@when("clico em uma notícia")
def clicar_noticia(context):
    context.web.find_element(By.XPATH, "//h3[contains(text(), 'Corinthians nunca perdeu para Felipão na Neo Química Arena; veja o retrospecto')]").click()

@then("verifico se sou redirecionado para outra página que mostra a mesma manchete")
def verificar_redirecionamento(context):
    manchete = context.web.find_element(By.XPATH, "//h1[contains(text(), 'Corinthians nunca perdeu para Felipão na Neo Química Arena; veja o retrospecto')]").text
    nova_pagina = context.web.current_url

    assert manchete in nova_pagina, "Redirecionamento incorreto"
