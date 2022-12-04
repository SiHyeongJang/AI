# 개발 환경
OS : window10 PC
Graphics Card : RTX 3090

# 도커
Docker version : 20.10.21, build baeda1f
CONTAINER Name : jsh
 : 아나콘다, cuda11.2, cudnn8.1, tensorflow=2.10.0


# Coding
1. 클린코드 관련
2. Process & Thread 폴더 - 파이썬 멀티 프로세싱 (함수 FOR문 돌리기 - multiprocessing 라이브러리 - pool 활용)

# AI
[Images]
1. stable-diffusion-tensorflow : 도커 환경을 통한 stable-diffusion 테스트 및 구현
2. Tesseract-OCR : 이미지 캡쳐 후 번역하기 (기능 : 전체화면 번역, 선택창 번역(선택하고R클릭), 범위 번역 (R~R-R클릭범위))
 -캡쳐 후 번역 프로그램 만들기 [Image 활용 (이미지 생성) -> Tesseract-OCR 활용 - 설치필요  (OCR : 이미지-> 영어 추출) -> googletrans 라이브러리 (구글 번역 : 영어-> 한글) -> tkinter 라이브러리 (GUI 구성)]
999. GDXRAY : 스마트 팩토리 관련 구현 확인(해당 GitHub 중단됨)
[DB]
1.MongoDB : UTC, KST 쉽게 Select하는 패키지 만들기

# Python
- 3.5 : type hint (typing ,mypy)
- 3.11.0b4 : Faster CPython : 이전 버전에 비해 (3.10) 전반적인 실행 속도가 10%~60% 정도, 평균적으로는 25% 정도 빨라짐
 -> https://www.python.org/downloads/release/python-3110b4/
