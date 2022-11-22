"""

def main(*args, **kwargs) -> any:
    print("Hello world!")

if __name__ == "__main__":
    main()

"""

import os

command: str = "python -m venv "
fp     : str = input("Name : ")

os.system(f'mkdir "{fp}"')
os.chdir(f"{fp}")

os.system(f'{command} "{fp} Dependancies"'  )
os.system('mkdir main')
with open("./main/main.py", 'w') as f:
    f.write(__doc__)

print("Finished creating virtual ENV...")