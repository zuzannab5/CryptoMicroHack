
import subprocess
import hashlib



def hash(input_flag):
    encoded_flag = input_flag.encode()
    obj_sha3_256 = hashlib.sha3_256(encoded_flag)
    return obj_sha3_256.hexdigest()

class App():
    def __init__(self):
        self.levels = 6

    def __wait_for_flag(self, flag):
        prompt = "Podaj flagę:\n"
        while True:
            input_flag = input(prompt)
            hash_input_flag = hash(input_flag)
            if not flag:
                break
            if hash_input_flag == flag:
                print("Udało ci się! :) ")
                print()
                break
            print("Podałeś złą flagę :( , spróbuj ponownie!")
    def __open_zadanie(self, path_to_task):
        subprocess.Popen([path_to_task],shell=True)

    def __zadania(self, level:int):
        flag = None

        if level == 1:
            self.__open_zadanie("Dodatki\\Zadanie_1\\task.pdf")
            flag = "f9aa6798eb46c7e2da6189473d64f80350fd929d8274d225aa435d4ed95d2f43"
        elif level == 2:
            self.__open_zadanie("Dodatki\\Zadanie_2\\task.pdf")
            flag = "763d2d42a62138d3dc7e1e5d503b9333f33a562939a60493e403f0f1d107e3d4"
        elif level == 3:
            self.__open_zadanie("Dodatki\\Zadanie_3\\task.pdf")
            flag = "3a4137897522d5db7d3138b23397830e60f3d4d255e515c2218b39bf747072e4"
        elif level == 4:
            self.__open_zadanie("Dodatki\\Zadanie_4\\task.pdf")
            print("Do rozwiązania potrzebny będzie plik /Dodatki/Zadanie_4/aes.py")
            flag = "56b9ba20a36f03233c6d8b8c934a4b24ed361007e6a881847481bfc47cbaefd9"
        elif level == 5:
            self.__open_zadanie("Dodatki\\Zadanie_5\\task.pdf")
            flag = "c72777c0da0231f1fc9a3fd753fec3a73543b3ae01aa67c259a9a643c4ae4e5e"
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
        print("Gratulacje! Udało ci się zrobić wszystkie zadania :)")
        print()
        with open("ending.txt", "r", encoding="utf-8") as f:
            logo = f.read()
        print(logo)
if __name__ == "__main__":
    app = App()
    app.run()
