smartphone = {
"brand": "Apple",
"device": "IPhone",
"model": "13 Pro Max",
"color": "Starlight"
}

smartphone.pop("brand")
del smartphone["device"]
#removes the item with the specified key name

print(smartphone)