from tqdm import tqdm
import schedule
import subprocess
import time

def executar_codigo():
    subprocess.run(["python", "main.py"])
    
schedule.every().day.at("08:50").do(executar_codigo)

while True:
    schedule.run_pending()
    time.sleep(60)