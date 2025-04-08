import pyautogui
import time
import pandas as pd

# Define uma pausa automática entre os comandos do pyautogui
pyautogui.PAUSE = 1

# Abre o navegador (Firefox)
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

# Aguarda o navegador abrir
time.sleep(3)

# Acessa o site
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")

# Aguarda o site carregar
time.sleep(5)

# Preenche o login
pyautogui.press("tab")
user = "pythonimpressionador@gmail.com"
pyautogui.write(user)
pyautogui.press("tab")

# Preenche a senha
senha = "sua_senha"  # Substitua por sua senha real com cuidado
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

# Aguarda o login ser concluído
time.sleep(5)

# Lê a tabela de produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Loop para preencher o formulário com os dados da planilha
for linha in tabela.index:
    pyautogui.click(x=808, y=264)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
       pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  # Envia o cadastro
    pyautogui.scroll(5000)
    
    time.sleep(2)
    

    
    
