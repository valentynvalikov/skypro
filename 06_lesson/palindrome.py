def is_palindrome(word):
    lower_word = word.lower()
    reversed_word = lower_word[::-1]
    if lower_word == reversed_word:
        return True
    else:
        return False


# код вашей функции должен быть выше

try:
    assert is_palindrome("level") is True
    assert is_palindrome("sagas") is True
    assert is_palindrome("hero") is False
    assert is_palindrome("drama") is False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")