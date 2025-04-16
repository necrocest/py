import time
from datetime import datetime,time

try:
    while True:
        ahora = datetime.now().strftime("%H:%M:%S") 
        print("\rHora actutal: {}".format(ahora), end =" ")
    
except KeyboardInterrupt:
    print("\nReloj interrumpido")