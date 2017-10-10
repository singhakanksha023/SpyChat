#THE THREE DICTIONARIES
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0], 
    "quizzes": [88.0, 40.0, 94.0],        
    "tests": [75.0, 90.0]                

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],           
    "tests": [89.0, 97.0]                   
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],    
    "quizzes": [0.0, 75.0, 78.0],           
    "tests": [100.0, 100.0]                
}
students=[lloyd,alice,tyler]           

# ALL THE FUNCTIONS ARE BELOW:-

def average(numbers):                  
    total=sum(numbers)
    total=float(total)
    result=total/len(numbers)
    return result                     

def get_average(student):              
    homework=sum(student["homework"])/len(student["homework"])
    quizzes=sum(student["quizzes"])/len(student["quizzes"])
    tests=sum(student["tests"])/len(student["tests"])
    return .1*homework+.3*quizzes+.6*tests  

def get_letter_grade(score):             
        if score>=90:
            return "A"
        elif score>=80:
            return "B"
        elif score>=70:
            return "C"
        elif score>=60:
            return "D"
        else:
            return "F"
def class_average(students):  
    results = []
    for student in students:
        r = get_average(student)
        results.append(r)
    return average(results)


print (class_average(students)
       ,get_letter_grade(class_average(students))) 