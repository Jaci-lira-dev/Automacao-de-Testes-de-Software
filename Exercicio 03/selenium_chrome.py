from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configura opções para o Chrome
options = Options()
options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inicializa o serviço e o driver do Chrome com as opções configuradas
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Acessa o site
driver.get('http://google.com.br')

# Maximiza a janela
driver.maximize_window()

# Imprime informações
print('Título:', driver.title)
print('Endereço URL:', driver.current_url)
print('Código Fonte (primeiros 100 caracteres):', driver.page_source[:100])

# Fecha o navegador
driver.quit()







