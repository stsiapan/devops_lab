list1 = ["5", "2", "C", "D", "+"]
point = []
lstep = list1.index("C")
step = 1
if list1.__sizeof__() > 1 & list1.__sizeof__() < 1000:
    for i in list1:
        if i == "C":
            point.pop()
            print("Operation {0}: The round {1}'s data is invalid. \
            The sum is: {2}".format(
                step,  lstep, (sum(point))))
            step = step + 1
        elif i == "D":
                point.append(point[-1] * 2)
                print("Round {0}: You could get {1} points (the round {2}'s data has been \
removed). The sum is: {3} ".format(lstep, point[-1], lstep, sum(point)))
        elif i == "+":
            point.append(point[-1] + point[-2])
            print("Round {0}: You could get {1} + {2} = {3} points. The sum is \
: {4}".format(lstep, point[-2], point[-3], point[-2] + point[-3], sum(point)))
        else:
            point.append(int(i))
            if point[-1] > -3000 & point[-1] < 3000:
                print("Round {0}: You could get {1} points. The sum \
                is: {2}".format(lstep, i, (sum(point))))
