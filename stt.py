from google.cloud import speech
import pyaudio
import requests
import os

file_name = "myfile.txt"  # 파일 이름
absolute_path = os.path.abspath("googlecredential.json")
print(absolute_path)

# Google Cloud 인증 정보 설정
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = absolute_path
def stream_audio():
    # 오디오 스트리밍 설정
    RATE = 16000  # 샘플링 레이트
    CHUNK = int(RATE / 10)  # 100ms 오디오 청크

    # PyAudio 초기화
    audio_interface = pyaudio.PyAudio()
    audio_stream = audio_interface.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    # 오디오 생성 함수
    def generate_audio():
        while True:
            data = audio_stream.read(CHUNK, exception_on_overflow=False)
            if not data:
                continue
            yield speech.StreamingRecognizeRequest(audio_content=data)

    # Google Cloud Speech 클라이언트
    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code="ko-KR",  # 한국어 설정
    )
    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True
    )

    # 스트리밍 API 호출
    responses = client.streaming_recognize(streaming_config, generate_audio())

    try:
        # 응답 처리
        for response in responses:
            for result in response.results:
                # 중간 결과도 포함
                if result.alternatives:
                    transcript = result.alternatives[0].transcript.strip()
                    print(f"중간 텍스트: {transcript}")
                    
                    # 단어별로 분리하여 처리
                    word = transcript.split()[-1]
                    if word == "왼쪽":
                        print("왼쪽으로 이동")
                        requests.get('http://localhost:8000/direction/left', json={'direction': 'left'})
                    elif word == "오른쪽":
                        print("오른쪽으로 이동")
                        requests.get('http://localhost:8000/direction/right', json={'direction': 'right'})
                    elif word == "아메리카노":
                        print("아메리카노 선택")
                        requests.get('http://localhost:8000/menu/ame', json={'menu': 'ame'})
                    elif word == "카페라떼" or word == "라떼":
                        print("카페라떼 선택")
                        requests.get('http://localhost:8000/menu/cl', json={'menu': 'cl'})
                    elif word == "카푸치노" or word == "치노":
                        print("카푸치노 선택")
                        requests.get('http://localhost:8000/menu/cc', json={'menu': 'cc'})
    except Exception as e:
        print(f"스트리밍 중 오류 발생: {e}")
    finally:
        # 리소스 정리
        audio_stream.stop_stream()
        audio_stream.close()
        audio_interface.terminate()

if __name__ == "__main__":
    stream_audio()
