while True:
    try:
        x = int(raw_input("please enter number!"))
        break
    except ValueError:
        print "not valid input!"

print x