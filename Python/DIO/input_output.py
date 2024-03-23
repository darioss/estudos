name = input("What is your name?\n")
age = input("What is your age?\n")
print(name, age, sep=" - ", end=" ...")

SERVICES = ["Administrative","Commercial","Support"]
select_service = input(f"Select 1 for {SERVICES[0]}, 2 for {SERVICES[1]} or 3 for {SERVICES[2]}\n")

if (int(select_service) == 1):
  print(f"{SERVICES[0]} is selected")
elif(int(select_service) == 2):
  print(f"{SERVICES[1]} is selected")
else:
  print(f"{SERVICES[2]} is selected")

