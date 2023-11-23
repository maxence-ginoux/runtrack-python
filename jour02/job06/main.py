for i in range(2, 1001):
    est_premier = True
    for f in range(2, int(i/2)):
        if i % f == 0:
            est_premier = False
            break
    if est_premier:
        print(i)