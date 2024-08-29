def calculate_bmi(weight, height):
    
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi
  
students = {
        'Alice': {'classs': 'A', 'height': 165, 'weight': 55, 'sport': 'Basketball', 'age': 16, 'activity_level': 'high', 'calorie_intake': 2200},
        'Bob': {'classs': 'B', 'height': 175, 'weight': 70, 'sport': 'Football', 'age': 17, 'activity_level': 'moderate', 'calorie_intake': 2500},
        'Charlie': {'classs': 'C', 'height': 180, 'weight': 85, 'sport': 'Swimming', 'age': 15, 'activity_level': 'low', 'calorie_intake': 2000}
    }   
    
def caloric_needs(weight, height, age, activity_level):
   
    b = 10 * weight + 6 * height 
    if activity_level == 'low':
        caloric_need = b * 1.1
    elif activity_level == 'moderate':
        caloric_need = b * 1.99
    elif activity_level == 'high':
        caloric_need = b * 2
    else:
        caloric_need = b  
    return caloric_need

def diet_feedback(cal, calorie_intake):
    if calorie_intake < cal*0.85:
        return 'Red: Underweight'
    elif calorie_intake < cal:
        return 'Orange: Needs more intake'
    else:
        return 'Green: Sufficient consumption'
    


def add_student(name ,classs , height , weight , sport , age , activity_level , calorie_intake ):
    students[name]={
        "classs":classs,
        "height":height,
        "weight":weight,
        "sport":sport,
        "age":age,
        "activity_level":activity_level,
        "calorie_intake":calorie_intake
    }
    
    
def manage_student_grades():
   
    for student, data in students.items():
        print(f"Student: {student}")
        bmi = calculate_bmi(data['weight'], data['height'])
        caloric = caloric_needs(data['weight'], data['height'], data['age'], data['activity_level'])
        feedback = diet_feedback(caloric, data['calorie_intake'])
        
        print(f"Class: {data['classs']}")
        print(f"Height: {data['height']} cm")
        print(f"Weight: {data['weight']} kg")
        print(f"Sport: {data['sport']}")
        print(f"BMI: {bmi:.2f}")
        print(f"Caloric Needs: {caloric}")
        print(f"Calorie Intake: {data['calorie_intake']}")
        print(f"Diet Feedback: {feedback}")
        print()



add_student('rishika' , 'D', 178 , 88 , 'Badminton' , 10 , 'low', 1000)    
manage_student_grades()    
    

              

        
    
    
    
    
    
    
    
    
    
