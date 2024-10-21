""""
Florheim Wizard V. Mariano
CS3B
Quiz No: 2
Date: October 11,2024
"""

# the value from studentName and classmateName stored into DICTIONARY LIST as studentInfo and classmateInfo
studentInfo = {
    "studentName": "Lewis Fonsi",
    "studentAddress": "City of Candon, Ilocos Sur",
    "studentFavNum": 25,
    "studentAge": 25,
    "studentAllowance": float(500)
}

classmateInfo = {
    "classmateName": "Andrea Andres",
    "classmateAddress": "City of Vigan, Ilocos Sur",
    "classFavNum": "18",
    "classmateAge": "21",
    "classmateAllowance": "700"
}

# Store the lengths of names in a list
studentsNameLengths = [len(studentInfo["studentName"]), len(classmateInfo["classmateName"])]

def Students(): #created callable function which contain IF ELSE Statement.
    if "Ilocos Sur" in studentInfo['studentAddress'] and "Ilocos Sur" in classmateInfo['classmateAddress']:
        print(f"Lewis Fonsi is from {studentInfo['studentAddress']}")
        print(f"Andrea Andres is from {classmateInfo['classmateAddress']}")
        if studentsNameLengths[0] > studentsNameLengths[1]:
            print(f"{classmateInfo['classmateName']} has a longer name than {studentInfo['studentName']} with {studentsNameLengths[1]} letters over {studentsNameLengths[0]} letters")
        else:
            print(f"{studentInfo['studentName']} has a longer name than {classmateInfo['classmateName']} with {studentsNameLengths[0]} letters over {studentsNameLengths[1]} letters")  
              
    elif "Ilocos Sur" in {studentInfo["studentAddress"]} and {classmateInfo["classmateAllowance"]}:
        sName_Split = studentInfo["studentName".split(" ")]
        cName_Split = classmateInfo["classmateName".split(" ")]
        print("One among {sName_Split[0]} or {cName_Split[0]} lives in Ilocos Sur")
    else:
        print("None of the students lives in Ilocos Sur")
Students() #Call the function Students() passingg a variable value 

# COMPUTATION OF THE AGE, ALLOWANCES, FAVNUMS  
print(f"The addded age of Lewis Fonsi and Andrea Andres is",studentInfo["studentAge"] + int(classmateInfo["classmateAge"]))  
print(f"The subtracted age of Lewis Fonsi and Andrea Andres is",studentInfo["studentAge"] - int(classmateInfo["classmateAge"]))  #print using fstring format: The subtracted favNum of studentFavNum and classmateFavNum, in subtraction to perform a mathematical

combinedWeeklyAllowance = studentInfo["studentAllowance"] + float(classmateInfo["classmateAllowance"])
print(f"The added allowance of Lewis Fonsi and Andrea Andres is {float(combinedWeeklyAllowance):.2f} pesos")  

classList = [studentInfo["studentName"],classmateInfo["classmateName"]]  
classList_Ext = [studentInfo["studentAddress"], classmateInfo["classmateAddress"]]  
classList.extend(classList_Ext)  

for i in classList:
    print(i)              #print out the value of the classLists using the for loop
    
classNumbers = [studentInfo["studentAge"], studentInfo["studentFavNum"], studentInfo["studentAllowance"]]  #Create a list cointaining all the numerical vars of the student, assure that all var are int 
classNumbers.append(int(classmateInfo["classmateAge"]))     #append the classmateAge, Note that the list must contain int var only
classNumbers.append(int(classmateInfo["classFavNum"]))   #append the classmateFavNum, Note that the list must contain int var only
classNumbers.append(int(classmateInfo["classmateAllowance"]))   #append the classmateAllowance, Note that the list must contain int var only
classNumbers.sort(reverse=True) #the sort() reversed of the classNumbers List

for i in classNumbers:
    print(i)            #print out the value of the classNumberes using the for loop
    

userName =input("Enter Your FULL NAME: ")  #promth the user to input the name of the username to pass the parameter to quizTwo(userName)

def quizTwo(studentNameCS):              #Create a simple function for QuizTwo() whichs receive a parameters studentNameCS
    print(f"Congratulations on Quiz 2 Refactoring! {studentNameCS}")     #Print wuth fstring format Ouput: Congratulations on Quiz 2 {passed variable}
quizTwo(userName)              #Call the function QuizTwo() passingg a variable value from the declared userName input