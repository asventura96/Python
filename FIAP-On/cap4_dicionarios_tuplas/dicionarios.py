usuarios = {}
print (usuarios)

usuarios = {
    "chaves" : ["Chaves do 8", "24/12/2017", "RECEP_01"],
    "quico" : ["Quico das Flores", "20/12/2017", "RAIOX_03"]
}

print (usuarios)

usuarios ["florinda"] = ["Dona Florinda", "24/12/2017", "RAIOX_01"]

print (usuarios)

print ("####----####")
print (usuarios.get("quico"))