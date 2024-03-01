def not_coming(guests):
    while True:
        reservation = input()
        if reservation == "END":
            break
        elif reservation in guests:
            guests.remove(reservation)
    print(len(guests), *sorted(guests), sep="\n")


invited_guests = {input() for i in range(int(input()))}
not_coming(invited_guests)
