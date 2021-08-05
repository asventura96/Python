from threading import Thread
import time

def carro(velociade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velociade
        time.sleep(0.5)
        print('Piloto: {} Km: {} '.format(piloto, trajeto))


t_carro1 = Thread(target = carro, args=[1, 'André'])
t_carro2 = Thread(target = carro, args=[1.5, 'Rafael'])

t_carro1.start()
t_carro2.start()