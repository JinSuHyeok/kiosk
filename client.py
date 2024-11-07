import requests
# pip install requets

while True:
    # 원래 소켓으로 조이스틱으로부터 데이터를 받아오는데, 지금은 테스트이므로 표준입력으로 대체 

    # 여기서 방향 받아옴, 실제로는 조이스틱에서 받아온 데이터로 대체 
    d = input("enter a direction, left or right: ")

    # 백엔드 서버로 요청 날리기 
    resp = requests.get(f"http://localhost:8000/direction/{d}")
