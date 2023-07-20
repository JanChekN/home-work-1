def is_palindrome(isp):
    return isp.lower() == isp.lower()[::-1]

is_pal = is_palindrome(input('Напишите текст для проверки на палиндром>> '))

if is_pal == True:
    print('Это палиндром')

else:
    print('Это не палиндром')