from behave import given, when, then
from selenium.webdriver.common.by import By

base_url = "https://www.atitus.edu.br/"

@when("eu acesso a página principal")
def acessar_site(context):
    context.web.get(base_url)

@then("deve ser mostrado um banner sobre vestibular no topo")
def banner_vestibular(context):
    vestibular = context.web.find_element(By.LINK_TEXT, "Vestibular de verão 2024/1. Inscreva-se agora mesmo!")


    
