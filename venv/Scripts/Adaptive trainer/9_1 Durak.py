"""
шите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>,
а на следующей строке указывается козырная масть.

Формат вывода:
Программа должна вывести слово
First, если первая карта бьёт вторую,
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.

Sample Input 1:

AH JH
D
Sample Output 1:

First
Sample Input 2:

AH JS
S
Sample Output 2:

Second
Sample Input 3:

7C 10H
S
Sample Output 3:

Error

"""

card_value = {'6': 0, '7': 1, '8': 2, '9': 3, '10': 4, 'J': 5, 'Q': 6, 'K': 7, 'A': 8}
cards = [card for card in input().split()]
trump = input()
if cards[0][1] == cards[1][1]:
    if card_value[cards[0][0]] > card_value[cards[1][0]]:
        print('First')
    else:
        print('Second')
elif cards[0][1] == trump or cards[1][1] == trump:
    if cards[0][1] == trump:
        print('First')
    else:
        print('Second')
else:
    print('Error')

