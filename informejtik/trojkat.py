print("wpisz dane do trójkata")
a = float(input())
b = float(input())
c = float(input())
if a + b > c and c + b > a and c + a > b:
    print("to jest trojkat")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
                print("to nie jest trojkat prostokatny")
    elif a == b == c:
        print("to nie jest trójkat rownoboczny")
    else:
            print("to nie jest trojkat prostokatny")
else:
    print("to nie jest trojkat")