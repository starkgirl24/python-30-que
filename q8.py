num = int(input("Enter Num for weekDay: ").strip())
match num:
    case 1: print("MON")
    case 2: print("tue")
    case 3: print("wed")
    case 4: print("thu")
    case 5: print("fri")
    case 6: print("sat")
    case 7: print("sun")
    case _: print("invalid")

    