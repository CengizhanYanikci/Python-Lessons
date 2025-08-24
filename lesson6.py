text="hello world"  #global variables
print(text)


def pythonlearn():
    text="Hello TON618" #local variables
    print("Arigato",text)

    notglobalvariables="hello jupiter" #not global (local variables)
    print(notglobalvariables)


    global nowglobalvariables # global
    nowglobalvariables ="hello moon" # global


pythonlearn()
print(text)
print(nowglobalvariables)
