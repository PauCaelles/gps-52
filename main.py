""" prova de CI/CD"""
import transform


def main():
    """ core del la prova"""
    string = input("Introdueix un string:")

    print("Quina transformació vols?")
    print("[1] Text amb tot majuscules")
    print("[2] Text amb tot minúscuies")
    print("[3] Text capitalitzat ")

    opcio = input("opció escollida: ")

    if opcio == "1":
        print(transform.to_upper_case(string))
    elif opcio == "2":
        print(transform.to_lower_case(string))
    elif opcio == "3":
        print(transform.to_capitalize(string))
    else:
        print("opció no reconegudda")


if __name__ == '__main__':
    main()
