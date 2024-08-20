#define button function

value_a = str(124+23-19)
value_1 = str

print(eval(value_a))


# Tests:
# 1. Part
# label = tkinter.Label(text="hello")
# label.place(x=200, y=0)
# 2. Part
# button = tkinter.Button(text="click me")
# button.place(x=100, y=30)
# 3. part
# entry = tkinter.Entry()
# entry.place(x=0,y= 60)



# another test
def button_calc2():
    value = str(counter["text"])
    if "+" in value:
        eco1 = value.split("+")
        result = int(eco1[0])
        count = len(eco1)
        for x in range(count - 1):
            result = result + int(eco1[x + 1])
    elif "-" in value:
        eco1 = value.split("-")
        result = int(eco1[0])
        count = len(eco1)
        for x in range(count - 1):
            result = result - int(eco1[x + 1])
    counter["text"] = result

n = 10%10

print(n)