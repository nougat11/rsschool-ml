def most_money(students):
    cost = 0
    change = 0
    name = ""
    for student in students:
        cc = student.fives * 5 + student.tens * 10 + student.twenties * 20
        if (cc >= cost):
            cost = cc
            name = student.name
    for student in students:
        cc = student.fives * 5 + student.tens * 10 + student.twenties * 20
        if (cc == cost):
            change += 1
    if change == len(students) and len(students) > 1:
        
        return "all"
    else:
        return name
        
