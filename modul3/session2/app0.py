# GET 2 numbers from user and calculate area in a function

def calculate_area():
    print("Calculate area for rectangle")
    length = int(input("provide length: "))
    width = int(input("provide width: "))
    area = length * width
    # print(area)
    return area

result = calculate_area()
print(result)
