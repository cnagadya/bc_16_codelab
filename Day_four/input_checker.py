while True:
    try:
        Name = str(raw_input("What is your name?"))
    except ValueError:
        print("Uhmmm, your name has got to be a string eg Christine ")
        
        continue
    else:
        #exiting loop if value is valid
        break
print("You are able to vote in the United States!" + name)
