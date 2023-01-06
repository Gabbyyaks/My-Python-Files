import phonenumbers
from number import number

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_numberv = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_numberv, "en"))

