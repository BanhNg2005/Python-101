answer = "Ronaldo"

def passwordgame():
    print("Chao mung ban den voi tro choi doan mat khau.")
    print("Co 5 luot doan thoi nhe ^_^")
    attempts = 5
    while attempts > 0:
        guess = input("Nhap mat khau: ").strip().lower().replace(" ", "")
        if guess == answer.lower().replace(" ", ""):
            if attempts >= 3:
                print("Ai da cung ghe day =))")
            elif 1 <= attempts < 3:
                print("Cung tam tam thoi. Lan sau choi tiep nha :>")
            break
        else:
            attempts -= 1
            print(f"Dung la chan be du, con co {attempts} luot doan nua thoi.")
            hint(attempts)
    else:
        print("Het luot nha ban oi :((")
        print(f"Dap an la: {answer}")
def hint(attempts):
    hints = {
        4: "Goi y 1: la 1 nguoi noi tieng tren the gioi",
        3: "Goi y 2: La 1 cau thu bong da",
        2: "Goi y 3: Tung hat bai 'Glory, glory Man United'",
        1: "Goi y 4: Siuuuuuuuu"
    }
    if attempts in hints: # Kiem tra xem so luot doan con lai co trong hints khong
        print(hints[attempts])

if __name__ == "__main__":
    passwordgame()