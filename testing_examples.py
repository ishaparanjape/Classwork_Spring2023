## testing should be done on the same branch as code

def area_ellipse(x: list):

    data = x.split(",")
    if len(data) = 1:
        area = math.pi * data[0]**2
    elif len(data) = 2:
        area = math.pi * data[0]**2
    return

## if a function has an input and output, TEST IT)
## input ex.: 20lb, 20LB, 20 lbs, 
def parse_weight(weight_input):
    # if input is an empty string
    if weight_input == "":
        return None
    # if there is no space between value and unit
    weight, units = weight_input.split(' ')
    weight = float(weight)
    # if an s is added after "lb" or "pound", the code removes it
    if units[-1] == "s":
        units = units[0:-1]
    # whatever is inputted will turn lowercase
    units = units.lower()
    if units in ["lb", "pound"]:
        weight_kg = convert_lb_to_kg(weight)
    elif units == "kg":
        weight_kg = weight
    else: 
        return None
    weight_kg = round(weight_kg)
    return weight_kg
        