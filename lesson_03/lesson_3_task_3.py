from address import Address
from mailing import Mailing


to_address = Address("152909", "Рыбинск", "ул. Куйбышева", "21", "10")
from_address = Address("111674", "Москва", "ул. 1-я Вольская", "22", "1")
cost = 250
track = 12345678

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
