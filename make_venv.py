"""

def main(*args, **kwargs) -> any:
    print("Hello world!")

if __name__ == "__main__":
    main()

"""
import os

command: str = "python -m venv " 
fp     : str = input("Name : ")
 
os.system(f'{command}"{fp}"'  )
os.system(f'mkdir "{fp} main"')
with open(f"./{fp} main/main.py", 'w') as f:
    f.write(__doc__)

print("Finished creating virtual ENV...")