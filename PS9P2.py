def score(p1, t1, p2, t2, p3, t3):
  score1 = float(p1/t1)
  score2 = float(p2/t2)
  score3 = float(p3/t2)
  tot = p1+p2+p3
  t = score1+score2+score3
  average = t/3*100
  return tot, average
  

lname = str(input("Enter student's last name: "))
p1 = int(input("Enter points earned on exam 1: "))
t1 = int(input("Enter total point for exam 1: "))
p2= int(input("Enter points earned on exam 3: "))
t2 = int(input("Enter total point for exam 2: "))
p3 = int(input("Enter points earned on exam 3: "))
t3 = int(input("Enter total point for exam 3: "))

tot, average = score(p1, t1, p2, t2, p3, t3)

print(lname, 'has', tot, 'total points and', str(average)+'% exam average')
