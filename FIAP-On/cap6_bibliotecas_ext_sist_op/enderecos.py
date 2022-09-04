from pygeocoder import Geocoder

endereco = 'Rua Engenheiro Carlos Goulart, 24, Belo Horizonte, MG'
resultado = Geocoder('AIzaSyAe0nr4xBd5S4PU9GtoQKib3v0urmF7sIY').geocode(endereco)
print(resultado)