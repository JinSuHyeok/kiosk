1. 깃허브에서 파일 가져오기 <br />

`git clone {깃허브 링크}`

<br /> <br />

2. 가상환경 만들기  <br />

`python -m venv venv`


3. 가상 환경 실행하기 <br />

윈도우 : `.\venv\Scripts\activate`
others : `source venv/bin/activate`
<br /> <br />
4. 가상환경 구축하기  <br />

`pip install -r requirements.txt`

 <br /> <br />



 5. 서버 실행하기  <br />

`python main.py`

 <br /> <br />

 6. 사이트 실행 <br />
 http://localhost:8000
 
 7. ipconfig (IPv4) <br />

 8. 폰에 http://localhost:8000/direction/left or right <br />
 

ngrok http 8000 입력후 http 부분 뺴서 복사
주소 찾아서 templates/index.html의 line 113줄에 주소 바꾸기 하고 crtl+s로 저장
wss
실행 후 서버 새로고침(ctrl c 누르고 python main.py 실행)
사이트 새로고침
