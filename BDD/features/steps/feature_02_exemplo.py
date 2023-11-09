from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://nubank.com.br/"

@given("que esteja na tela inicial")
def acessar_site(context):
    context.web.get(base_url)

@when('preencho campo de cpf com um valor inválido: "{cpf}"')
def step_impl(context, cpf):    
    context.web.find_element(By.ID, "field-cpf").clear()
    context.web.find_element(By.ID, "field-cpf").send_keys(cpf)

@then('verificar se é disparada a mensagem "{msg}"')
def valida_msg(context, msg):      
    try:
        p_cpf_error = WebDriverWait(context.web, 10).until(EC.presence_of_element_located((By.ID, "error-cpf")))

        return True if p_cpf_error.text == msg.strip() else False
    except NoSuchElementException:
        raise AssertionError('Elemento não encontrado')