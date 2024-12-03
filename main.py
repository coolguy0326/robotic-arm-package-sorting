def sort(width, height, length, mass):
    volume = width * height * length

    is_bulky = (volume >= 1000000) or (width >= 150 or height > 150 or length > 150)

    is_heavy = mass > 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

print(sort(100, 100, 100, 10))
print(sort(150, 150, 150, 25))
print(sort(50, 50, 50, 25))
print(sort(50, 50, 50, 5))