
import threading
import time

def simular_download(nome_arquivo, tempo):
    print(f"Iniciando download de {nome_arquivo}...")
    time.sleep(tempo)
    print(f"Download de {nome_arquivo} concluído em {tempo}s.")

arquivos = [
    ("arquivo1.zip", 3),
    ("arquivo2.zip", 5),
    ("arquivo3.zip", 2)
]

threads = []

for nome, tempo in arquivos:
    t = threading.Thread(target=simular_download, args=(nome, tempo))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("✅ Todos os downloads foram concluídos.")
