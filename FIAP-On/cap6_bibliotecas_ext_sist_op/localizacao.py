from pygeocoder import Geocoder

endereco = '24, Engenheiro Carlos Goulart, Belo Horizonte, MG'
print(Geocoder('AIzaSyAe0nr4xBd5S4PU9GtoQKib3v0urmF7sIY').geocode(endereco).coordinates)