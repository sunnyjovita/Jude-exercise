def convert_to_days():
    ho = eval(input("Enter number of hours :"))
    min = eval(input("Enter number of minutes : "))
    sec = eval(input("Enter number of seconds : "))
    total = round((ho/24)+(min/1440)+(sec/86400),4)
    print("The number of days :" +str(total))

def calc_weight_on_planet(w, g=23.1):
    weight = (w/9.8)*g
    print(weight)

def num_atoms(n, mr=196.97 ):
    atoms_weight = (n/mr)*6.022e23
    print(atoms_weight)

def calc_new_height():
    cw = eval(input("Enter the current width : "))
    ch = eval(input("Enter the current height : "))
    dw = eval(input("Enter the desired width : "))
    dh = (dw/cw)*ch
    print("The corresponding height is :" +str(dh))

def convert_temp():
    Farenheit = eval(input("Enter the temperature in Fahrenheit : "))
    print("The temperature in fahrenheit is :" +str(Farenheit))
    convert_to_celcius(Farenheit)
def convert_to_celcius(farenheit):
    celcius = (farenheit-32)*5/9
    print("The temperature in celcius is : " +str(celcius))
    convert_to_kelvin(celcius)
def convert_to_kelvin(celcius):
        kelvin = celcius + 273.15
        print("The temperature in kelvin is :" +str(kelvin))






    # print("The temperature in Fahrenheit is :" +str(Tf))
    # print("The temperature in Celcius is :" +str(Tc))





