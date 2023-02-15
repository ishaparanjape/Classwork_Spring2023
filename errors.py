#a = "The sky is blue"
#print(a)

#for letter in a:
#    print(let)

    

def my_function(a, b):
    try:
        c = sum(a,b)
    except IOError:
        a = 2
        b = 3
        c = sum(a,b)
    return c
    
def main():
    my_function(2, 3)
    print(c)

    

if __name__ == "__main__":
    main()

def calc_square_root(n):
    try:
        from my_math_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt
    answer = sqrt(n)
    return answer

def main():
    x = 4
    try:
        answer = calc_square_root(x)
        x = answer + 5
        if x > 10:
            
    except TypeError:
        new_x = int(x)
        answer = calc_square_root(new_x)
    except ValueError:
        print("You must send a number")
        answer = ""
    else:
        print("There was no error")
    print(answer)

if __name__ == "__main__":
    main()