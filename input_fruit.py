# first input file
in_file = open("input_data.txt", "r")
fruits = in_file.readlines()
print(fruits)
in_file.close() #closes the input_data.txt file, but still keeps the values stored in fruits
print(fruits)

in_file = open("input_data.txt", "r")

first_fruit = in_file.readline()
second_fruit = in_file.readline()
print(first_fruit)
print(second_fruit)


# second input file
def analyze_ID(input_line):
    patient_data = first_line.strip("\n").split("=")
    patient_id = int(patient_data[1])
    return patient_id


def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    id = analyze_ID(first_line)



def test_read_file():
    from module import read_file
    filename = "input_file.txt"
    answer = read_file(filename)
    expected = 50
    assert == expected 