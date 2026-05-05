data = {
    "A101": {"name": "Ravi", "marks": {"math": 78, "cs": 83, "eng": 69}},
    "A102": {"name": "Sneha", "marks": {"math": 92, "cs": 89, "eng": 94}},
    "A103": {"name": "Arjun", "marks": {"math": 55, "cs": 61, "eng": 47}},
    "A104": {"name": "Meera", "marks": {"math": 88, "cs": 72, "eng": 80}}
}

for roll_no in data:
    marks = data[roll_no]["marks"]
    total = marks["math"] + marks["cs"] + marks["eng"]
    percentage = (total / 300) * 100
    
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
        
    data[roll_no]["total"] = total
    data[roll_no]["percentage"] = percentage
    data[roll_no]["grade"] = grade

highest_score = 0
highest_scorer = ""
for roll_no in data:
    if data[roll_no]["total"] > highest_score:
        highest_score = data[roll_no]["total"]
        highest_scorer = data[roll_no]["name"]

math_highest = 0
math_topper = ""
cs_highest = 0
cs_topper = ""
eng_highest = 0
eng_topper = ""

for roll_no in data:
    marks = data[roll_no]["marks"]
    name = data[roll_no]["name"]
    
    if marks["math"] > math_highest:
        math_highest = marks["math"]
        math_topper = name
        
    if marks["cs"] > cs_highest:
        cs_highest = marks["cs"]
        cs_topper = name
        
    if marks["eng"] > eng_highest:
        eng_highest = marks["eng"]
        eng_topper = name

list_of_dicts = []
for roll_no in data:
    student_info = data[roll_no]
    student_info["roll_no"] = roll_no
    list_of_dicts.append(student_info)

n = len(list_of_dicts)
for i in range(n):
    for j in range(0, n-i-1):
        if list_of_dicts[j]["percentage"] < list_of_dicts[j+1]["percentage"]:
            temp = list_of_dicts[j]
            list_of_dicts[j] = list_of_dicts[j+1]
            list_of_dicts[j+1] = temp

roll_grade_mapping = {roll_no: data[roll_no]["grade"] for roll_no in data}

print("Highest Scorer:", highest_scorer)
print("Math Topper:", math_topper)
print("CS Topper:", cs_topper)
print("English Topper:", eng_topper)
print("Sorted List of Dictionaries:", list_of_dicts)
print("Roll No to Grade Mapping:", roll_grade_mapping)