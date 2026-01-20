name = (input("the employee name :"))
salary = int(input( "monthly salary :"))
preformance_score = int (input("preformance :"))
late_days= int(input("late days :"))
years_in_company= int(input( "years of experience in company :"))

bonus = salary *.15 if preformance_score >= 80 else 0
final_salary = salary + bonus 

good_attendence = late_days <= 2 
experinced = years_in_company >= 4 

if preformance_score >= 90 :
    grade = "A"
elif preformance_score >= 80 :
    grade = "B"
elif preformance_score >= 70 : 
    grade = "C"
elif preformance_score >= 60 : 
    grade = "D"

if preformance_score >= 80 and good_attendence : 
    bonus_status = "eligble for bonus"
elif preformance_score >= 80 and not good_attendence :
    bonus_status = "preformance good , attendence issue "
else :
    bonus_status = "not eligible for bonus"

if grade == "D" and late_days >= 6:
    status = "worning Issued"
else :
    status = "good standing"

print (f"""
employee report :
--------------------
name : {name}
preformance : {preformance_score}       
grade : {grade}

base salary : {salary}
bonus : {bonus}
final salary : {final_salary}

attendance : {late_days} late days
experience : {years_in_company} years 

bonus stastus : {bonus_status}
overall status : {status}
""")


