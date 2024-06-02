
import subprocess
import sys

class App():
    def __init__(self):
        self.levels = 6

    def __wait_for_flag(self, flag):
        prompt = "Podaj flagę:\n"
        while True:
            input_flag = input(prompt)
            if input_flag == flag:
                print("Udało ci się :) !")
                break
            print("Podałeś złą flagę :( , spróbuj ponownie!")
    def __open_zadanie(self, path_to_task):
        subprocess.Popen([path_to_task],shell=True)

    def __zadania(self, level:int):
        flag = ""

        if level == 1:
            self.__open_zadanie("Dodatki\\Zadanie_1\\task.pdf")
            flag = "Snowman jest super"
        elif level == 2:
            pass
        elif level == 3:
            pass
        elif level == 4:
            self.__open_zadanie("Dodatki\\Zadanie_4\\task.pdf")
            print("Do rozwiązania potrzebny będzie plik /Dodatki/Zadanie_4/aes.py")
            flag = "\\x81"
        elif level == 5:
            pass
        self.__wait_for_flag(flag)
        
    def run(self):
        with open("logo.txt", "r", encoding="utf-8") as f:
            logo = f.read()
        print(logo)
        _ = input()
        
        for level in range(1, self.levels):
            print()
            print("---------------------------------------------")
            print(f"Zapnij pasy! Zaczynamy zadanie {level}!")
            self.__zadania(level)
            print("---------------------------------------------")
        print("Gratulacje, udało ci się zrobić wszystkie zadania :)!")

if __name__ == "__main__":
    app = App()
    app.run()
