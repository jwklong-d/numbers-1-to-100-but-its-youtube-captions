value = 0
duration1 = ("0", "0", "0")
a = ()
second1 = 0
minute1 = 0
hour1 = 0
msstart = 0
duration2 = ("0", "0", "0")
a1 = ()
hour2 = 0
minute2 = 0
second2 = 0
msstart1 = 100
a2 = ()
valueend = input("Please enter number of captions:")

print("Progessing... Please wait.")

while value < int(valueend):
    value += 1
    msstart += 100
    msstart1 += 100

    if msstart >= 1000:
        msstart = 0
        second1 += 1

    if msstart1 >= 1000:
        msstart1 = 0
        second2 += 1

    if second1 >= 60:
        second1 = 0
        minute1 += 1

    if second2 >= 60:
        second2 = 0
        minute2 += 1

    if minute1 >= 60:
        minute1 = 0
        hour1 += 1

    if minute2 >= 60:
        minute2 = 0
        hour2 += 1

    duration1 = (str(hour1), str(minute1).zfill(2), str(second1).zfill(2))
    a = (":".join(duration1), str(msstart).zfill(3))
    duration2 = (str(hour2), str(minute2).zfill(2), str(second2).zfill(2))
    a1 = (":".join(duration2), str(msstart1).zfill(3))
    a2 = (".".join(a), ".".join(a1))
    
    print(
        ",".join(a2)
    )
    print(value)
    print("")