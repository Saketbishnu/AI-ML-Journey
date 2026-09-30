color = input("Enter colour: ")
match color:
    case "red":
        print("stop the car")
    case "yellow":
        print("look here")
    case "green":
        print("go")
    case _: ## default case
        print("invalid color")