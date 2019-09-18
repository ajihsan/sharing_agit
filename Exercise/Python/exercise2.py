"""
Ubah variable sehingga output print:
1
2
3
4
5
6
"""

# ubah variable ini
number = 10
second_number = 10
first_array = []
second_array = [1,2,3,4]

if number < 15 and number % 6 == 0:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number and number**2 > 200:
    print("6")
    
