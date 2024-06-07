def løs(tall, rester):
    # euklids algoritme
    def utvidet_euklid(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = utvidet_euklid(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    # Beregner modulær invers
    def modul_invers(a, m):
        gcd, x, _ = utvidet_euklid(a, m)
        if gcd != 1:
            print("invers no worky")
        return x % m

    # Løser CRT
    def løs_crt(tall, rester):
        produkt = 1
        for t in tall:
            produkt *= t

        resultat = 0
        for t_i, r_i in zip(tall, rester):
            p = produkt // t_i
            resultat += r_i * modul_invers(p, t_i) * p

        return resultat % produkt

    return løs_crt(tall, rester)

tall = [17, 16, 15]
rester = [3, 10, 0]
print(løs(tall, rester))
