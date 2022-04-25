from lesson6.validators.validate_pin import validate_pin
from lesson6.validators.validate_card import validate_card


print("Введите ваш номер карты")
card_number = input()
print("Введите ваш пин-код")
card_pin = input()


if validate_card(card_number):
    print('Номер карты допустимый')
else:
    print('Номер карты недопустимый')


if validate_pin(card_pin):
    print('Пин код допустимый')
else:
    print('Пин код недопустимый')
