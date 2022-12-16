def avscore(s1, s2, s3, handicap):
  t = s1+s2+s3
  average = t/3
  haverage = (t+handicap)/3
  return average, haverage

lname = str(input("Enter bowler's last name: "))
s1 = int(input("Enter score 1: "))
s2 = int(input("Enter score 2: "))
s3 = int(input("Enter score 3: "))
handicap = float(input("What is your handicap?: "))
average, haverage = avscore(s1, s2, s3, handicap)

print(lname+"'s average:", average, "and average with handicap:", haverage)
