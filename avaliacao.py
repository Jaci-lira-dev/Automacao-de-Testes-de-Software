from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def main():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    # chrome_options.add_argument("--headless")  # descomente para rodar sem abrir janela
    chrome_options.add_argument("--remote-debugging-port=9222")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("http://127.0.0.1:3000/avaliacao.html")

        element_nome = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "nome"))
        )
        element_nome.send_keys("Jaci Oliveira de Lira")
        time.sleep(2)

        element_ra = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "ra"))
        )
        element_ra.send_keys("2301725")
        time.sleep(2)

        element_data = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "data-nascimento"))
        )
        element_data.send_keys("01-08-1970")
        time.sleep(2)

        select_curso = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "curso"))
        ))
        select_curso.select_by_value("ads")
        time.sleep(2)

        select_nota = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nota"))
        ))
        select_nota.select_by_value("9")
        time.sleep(2)

        element_sugestoes = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sugestoes"))
        )
        element_sugestoes.send_keys("Que os alunos tenham a oportunidade de desenvolver um projeto completo a partir do zero, com o professor atuando como mentor (coach). A cada aula, uma nova funcionalidade prática aprendida deve ser incorporada ao projeto, promovendo uma aplicação direta dos conteúdos abordados."
        )
        time.sleep(2)

        element_obs = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "obs"))
        )
        element_obs.send_keys("O professor demonstra ampla experiência e consegue transmitir seus conhecimentos de forma clara e didática.")
        time.sleep(2)  
        
        botao_enviar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        botao_enviar.click()
        time.sleep(2)

        # Trata o alerta que aparece após enviar o formulário
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

        time.sleep(10)  # espera para visualizar

        with open("pagina_carregada.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
            time.sleep(10)
        
    finally:
        driver.quit()
        time.sleep(30)

if __name__ == "__main__":
    main()
