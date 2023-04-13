print("escolha sua bebida para o cade da manha")
bebida = input().lower()
match bebida:
    case "cafe":
        print("cuidade com o excesso de cafeina")
    case "leite":
        print("bom para os ossos")
    case "cha":
        print("acalma a mente")
    # case other: 
    case _:
        print("cada um tem seu gosto")