from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.magazineluiza.com.br/"

@given("que esteja na página inicial da Magazine")
def acessar_site(context):
    context.web.get(base_url)

@when("digito 'computador' no campo de busca e clico em pesquisar")
def pesquisar_produto(context):
    context.web.find_element(By.ID, "inpHeaderSearch").send_keys("computador")
    context.web.find_element(By.ID, "btnHeaderSearch").click()

@then("verifico se a página de resultados de busca é exibida")
def verificar_resultados_busca(context):
    resultados = context.web.find_elements(By.XPATH, "//div[@class='productShowCase']//li[@class='product']")

    assert len(resultados) > 0, "Nenhum resultado de busca encontrado"
