

def example():
    print("2^p = 1, ile wynosi p? ")
    flag = "CRYPTO"
    return flag


class App():
    def __init__(self):
        self.levels = 5

    def __wait_for_flag(self, flag):
        prompt = "Podaj flagę:\n"
        while True:
            input_flag = input(prompt)
            if input_flag == flag:
                print("Udało ci się :) !")
                break
            print("Podałeś złą flagę :( , spróbuj ponownie!")

    def __zadania(self, level:int):
        flag = ""

        if level == 0:
            flag = example()
        elif level == 1:
            pass
        elif level == 2:
            pass
        elif level == 3:
            pass
        elif level == 4:
            pass
        self.__wait_for_flag(flag)
        
    def run(self):
        with open("logo.txt", "r", encoding="utf-8") as f:
            logo = f.read()
        print(logo)
        for level in range(self.levels):
            print()
            print("---------------------------------------------")
            print(f"Zapnij pasy! Zaczynamy zadanie {level + 1}!")
            self.__zadania(level)
            print("---------------------------------------------")
        print("Gratulacje, udało ci się zrobić wszystkie zadania :)!")

if __name__ == "__main__":
    app = App()
    app.run()