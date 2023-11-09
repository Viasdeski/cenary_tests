from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.saucedemo.com/"

@given("que esteja na tela inicial do Sauce Demo")
def acessar_site(context):
    context.web.get(base_url)

@when('preencho o campo de usuário com "{usuario}"')
def preencher_usuario(context, usuario):
    username_input = context.web.find_element(By.ID, "user-name")
    username_input.clear()
    username_input.send_keys(usuario)

@when('preencho o campo de senha com "{senha}"')
def preencher_senha(context, senha):
    password_input = context.web.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(senha)

@when("clico no botão de login")
def clicar_login(context):
    login_button = context.web.find_element(By.ID, "login-button")
    login_button.click()

@then("verificar se sou redirecionado para a página principal logado na minha conta")
def verificar_redirecionamento(context):
    WebDriverWait(context.web, 10).until(EC.url_contains("inventory.html"))
