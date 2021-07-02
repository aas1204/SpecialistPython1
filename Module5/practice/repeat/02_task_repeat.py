# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    n_str=str(number)
    n_rev=n_str[::-1]
    return n_str==n_rev


print(palindrome(234532))
print(palindrome(765467))
print(palindrome(56765))
print(palindrome(12345321))
print(palindrome(9876789))
