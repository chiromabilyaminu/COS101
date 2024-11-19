def math_formula_option():
    print('\nMaths formula option:')
    print('a. perimeter of a triangle')
    print('b. area of a square')
    print('c. area of a sector')
    print('d. hypotenuse of a right angled triangle')
    print('e. area of a rhombus')

math_formula_option()

options = input('pick an option from a to f  ')
print(options)

if options == 'a':
    A = int(input('Enter number  '))
    B = int(input('Enter number  '))
    C = int(input('Enter number  '))
    perimeter = A + B + C
    print(perimeter)

elif options == 'b':
    side = int(input('Enter side of square  '))
    area = side ** 2
    print(area)

elif options == 'c':
    radius = int(input('Enter value for radius  '))
    angle = int(input('Enter value of the angle  '))
    area_of_a_sector = (angle / 360) * 22/7 * (radius ** 2)
    print(area_of_a_sector)

elif options == 'd':
    opposite = int(input('enter value for opposite  '))
    adjacent = int(input('enter value for adjacent  '))
    hypotenuse = (opposite ** 2) + (adjacent ** 2)
    print(hypotenuse)

elif options == 'e':
    d1 = int(input('enter d1  '))
    d2 = int(input('enter d2  '))
    area_of_rhombus = 0.5 * d1 * d2
    print(area_of_rhombus)

else :
    print('invalid option an option from a to f')