def main():
    print("Welcome to the Fluid Quality Checker!")
    
    # Step 1: Get Density
    density = Density()
    
    # Step 2: Get Temperature
    temperature = TEMPERATURE()
    
    # Step 3: Get Constant Temperature
    cons_temp = ConsTEMP()
    
    # Step 4: Calculate Temperature at STP
    temp_stp = TEMP_STP(temperature, cons_temp)
    print(f"Step 4: Calculated Temperature at STP: {temp_stp:.2f}°C")
    
    # Step 5: Calculate Final Temperature
    calcu_temp = Calcu_TEMP(temp_stp)
    print(f"Step 5: Calculated Final Temperature: {calcu_temp:.2f}")
    
    # Step 6: Determine Fluid Quality
    Good_BAD_FLUID(density, calcu_temp)

def Density():
    density = float(input("Step 1: What's the value measured for Density? "))
    return density

def TEMPERATURE():
    temperature = float(input("Step 2: What's the value measured for Temperature? "))
    return temperature

def ConsTEMP():
    # Assuming a constant temperature value of 15
    cons_temp = 15.0
    print(f"Step 3: Constant Temperature (ConsTEMP) is set to {cons_temp:.2f}°C")
    return cons_temp

def TEMP_STP(temperature, cons_temp):
    return temperature - cons_temp

def Calcu_TEMP(temp_stp):
    fluid_value = float(input("Step 5: Enter the value of the fluid measured: "))
    return temp_stp * fluid_value

def Good_BAD_FLUID(density, calcu_temp):
    total_value = density + calcu_temp
    print(f"Total Value for Fluid Quality Assessment: {total_value:.2f}")
    
    if total_value >= 900:
        print("Result: BAD FUEL")
    elif total_value >= 800:
        print("Result: GOOD FUEL - READY FOR OFFLOAD")
    elif total_value >= 700:
        print("Result: GOOD FUEL - READY FOR OFFLOAD")
    else:
        print("Result: BAD FUEL")

if __name__ == "__main__":
    while True:
        main()
        cont = input("Do you want to check another fluid? (yes/no): ")
        if cont.lower() != 'yes':
            break 