smartphone = {
"brand": "Apple",
"device": "IPhone",
"model": "13 Pro Max"
}

x = smartphone.items()

print(x)

if "model" in smartphone:
  print("Yes, 'model' is one of the keys in the smartphone dictionary")