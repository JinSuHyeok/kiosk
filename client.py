import requests

d = input("enter a direction, left or right: ")

resp = requests.get(f"http://localhost:8000/direction/{d}")
