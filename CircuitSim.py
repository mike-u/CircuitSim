r1 = 100.0
r2 = 400.0
r3 = 800.0
r4 = 600.0
r5 = 200.0
r6 = 0.0

x=0 #binary true false if current in 5 is above 2 mA

print "state", 'I5','X'

for stateA in range(0, 64):
    statebinstr = str(bin(stateA))
    statebinstr=statebinstr[2:]
    statebinstrL = len(statebinstr)

    while statebinstrL < 6:
        statebinstr = '0'+statebinstr
        statebinstrL = len(statebinstr)

    state = [statebinstr[0], statebinstr[1], statebinstr[2], statebinstr[3], statebinstr[4], statebinstr[5]]

    s1 = int(state[0])
    s2 = int(state[1])
    s3 = int(state[2])
    s4 = int(state[3])
    s5 = int(state[4])
    s6 = int(state[5])

    V = 5.0
    i5=0

    r123inv = 0.0
    r456inv = 0.0
    r123 = 0.0
    r456 = 0.0

    if (s1==1 and r1==0) or (s2==1 and r2==0) or (s3==1 and r3==0):
        r123=0
        #print("short circuit in 123")
    else:
        if s1 == 1 and r1 != 0:
            r123inv += 1/r1
          #  print ("r1 is on")
        if s2 == 1 and r2 != 0:
            r123inv += 1/r2
           # print("r2 is on")
        if s3 == 1 and r3 != 0:
            r123inv += 1/r3
          #  print("r3 is on")

    if r123inv != 0:
        r123 = 1/r123inv

    if (s4==1 and r4==0) or (s5==1 and r5==0) or (s6==1 and r6==0): #1 for s values means closed
        r456 = 0
     #   print("short circuit in 456")
    else:
        if s4 == 1 and r4 != 0:
            r456inv += 1/r4
        if s5 == 1 and r5 != 0:
            r456inv += 1/r5
        if s6 == 1 and r6 != 0:
            r456inv += 1/r6

    if r456inv != 0:
        r456 = 1/r456inv

   # print (r123, r456)
    if r123 != 0 or r456 != 0:
        R = r123+r456
        I = V/R
     #   print I

    if r456 != 0:
        i456 = I
        v456 = i456*r456
        v5 = v456
        i5 = v5/r5

    if i5 <= .02:
        x=1
    else:
        x=0
    print statebinstr, "%.3f" % i5, x
print("end")