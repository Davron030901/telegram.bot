import json

x = 10
x_json = json.dumps(x)

ism = "anvar"
ism_json = json.dumps(ism)

b=True
c=json.dumps(b)
print(type(x))
sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)
print(json.loads(c))
print(sonlar_json)

bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor)

print(bemor_json)

bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)
filename = 'bemor.json'
with open(filename,'w') as f:
  json.dump(bemor, f, indent=4)
filename = 'sonlar.json'
with open(filename,'w') as f:
  json.dump(sonlar, f)

sonlar = json.loads(sonlar_json)
bemor = json.loads(bemor_json)
print(bemor)

bemor2=json.loads(bemor_json)
print(bemor2)

sonlar2=json.loads(sonlar_json)

print(type(bemor))

with open(filename) as f:
  json.load(f)
