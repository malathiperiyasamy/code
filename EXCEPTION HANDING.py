print(" EXCEPTION HANDLING")
print("***********************")

#Exception handling
def divide_module():
    try:
       num1=int(input("Enter the Numerator:"))
       num2=int(input("Enter the Demoniator:"))
       result=num1/num2
       print("Result",result)

    except ZeroDivisionError:
        print("Invalid number divided by zero")
    except ValueError:
        print("Error divide by zero is not allowed")
    except:
        print("Error:enter the invalid input")
    finally:
        print("Program is successfully completed")

#Function calling
divide_module()


