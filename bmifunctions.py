import math

def pounds_to_kg(pounds_value):
    '''This function converts weight in pounds to kg
    Args: takes in a value in pounds(lbs).
    result: Returns single value in kgs.'''
    return (float(pounds_value) * 0.45359237)


def kg_to_pounds(kg_value):
    '''This function converts weight in kg to pounds
    Args: takes in a value in kilogram (kg).
    result: Returns single value in pounds.'''
    return (float(kg_value) * 2.2046226218)


def cm_to_feet_inches(cm_value):
    '''This function converts the height in cm to feet and inches 
    Args: takes in a value in cm.
    result: Returns two values, a tuple. A value in feet and another for inches.'''
    converted_value = float(cm_value) / 30.48
    inch_value, foot_value = math.modf(converted_value)
    #modf returns two values decimal and integer aspects
    # math.modf(100.12) returns  (0.12000000000000455, 100.0)
    inch_value = inch_value *12
    
    return (foot_value , inch_value)


def feet_inches_to_cm(feet_value_tuple):
    '''This function converts the height in feet and inches to centimeters 
    Args: takes in a tuple of values (feet,inches)  in feet and inches 
    result: height in cm.'''

    if type(feet_value_tuple) == tuple:
        foot_value, inch_value  = feet_value_tuple
        new_foot_value = foot_value * 30.48
        new_inch_value = inch_value * 2.54
        
        return (new_foot_value + new_inch_value)


def cm_to_meters(cm_value):
    '''This function converts height in cm to meters
    Args: takes in a value in centimeters (cm).
    result: Returns single value in meters.'''
    return (float(cm_value) / 100.0)


def calculate_bmi(weight, height):
    '''This function calculates the BMI
    Args: weight in kilograms & height in meters
    result: bmi and rating value ie. Overweight, Underweight.'''
    #BMI = Weight in KG/ (Height in Meters^2)
    bmi = weight / (height**2)
    if bmi < 18.5:
        rating = 'Under'
    if bmi >= 18.5 and bmi <= 25:
        rating = 'Normal'
    if bmi >= 25 and bmi < 30:
        rating = 'Over'
    if bmi >= 30:
        rating = 'Obese'    
    return(bmi, rating)


def get_ratings():
   ratings = 'Less than 18.5 = Underweight; Between 18.5 - 24.9 = Healthy Weight; Between 25 - 29.9 = Overweight; Over 30 = Obese'
   return(ratings)


if __name__ == '__main__':
    print("Please enter your height in ft like 5 or 6. note: If you are 5'6 or 6'0 or etc, please enter only 5 or 6.")
    height_feet = float(input())
    print("Please enter the inches portion of your height. Note: If you are 5'6 or 6'0 or etc, please enter only 6 or 0.")
    height_inches = float(input())
    
    #convert height from ftandinches to meters
    height = (height_feet, height_inches)
    height = feet_inches_to_cm(height)
    print(height)
    height = cm_to_meters(height)

    print('Please enter your weight in kg')
    weight = float(input())


    print('Your weight:',weight,'kg.',' Your height: ',height_feet,'ft ', height_inches,'inches')
    
    bmi, rating = calculate_bmi(weight, height)
    print ('Your bmi is: ',bmi)
    print('Interpretation: ',get_ratings())