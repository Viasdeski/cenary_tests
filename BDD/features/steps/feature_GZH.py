from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://gauchazh.clicrbs.com.br/"

@given("que esteja na tela inicial do Gauchazh")
def acessar_site(context):
    context.web.get(base_url)

@when("clico em uma categoria")
def clicar_categoria(context):
    categoria = context.web.find_element(By.CSS_SELECTOR, "div.topic-item a")
    categoria.click()

@then("verifico se sou redirecionado para a categoria selecionada")
def verificar_redirecionamento(context):
    current_url = context.web.current_url
    assert "https://gauchazh.clicrbs.com.br/esportes/brasileirao/ultimas-noticias" in current_url, "Não redirecionado para a categoria selecionada"
