from smartphone import Smartphone

catalog = [
    Smartphone("samsung", "Note 10+", "+79101234567"),
    Smartphone("oppo", "reno", "+79109876543"),
    Smartphone("apple", "16pro", "+79151234567"),
    Smartphone("honor", "x6b", "+79109876545"),
    Smartphone("realme", "Note 50", "+79151234562")

]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model} - {smartphone.number}")
