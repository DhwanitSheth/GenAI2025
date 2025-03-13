Prject Eular Problem #9

    # a + b + c = 12
    # a^2 + b^2 = c^2
    def trail():
        for a in range(1, 12):
            for b in range(1, 12):
                for c in range(1, 12):
                    print(f"checking with a = {a}, b = {b}, c = {c}")
                    if a + b + c != 12:
                        continue
                    if (a*a) + (b*b) != (c*c):
                        continue
                    print(f"a = {a}, b = {b}, c = {c}")
                    return

    trail()


