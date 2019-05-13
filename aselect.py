import random
from datetime import datetime

def main():
    date = datetime.now().strftime("%Y-%m-%d")
    print("Never mind what you choose, just do it!")
    choices = ["Resto Druid", "Walnut", "SoloHealer"]
    choice = random.choice(choices)
    print("[{}] Today, your choice is {}.".format(date, choice))


if __name__ == '__main__':
    main()
