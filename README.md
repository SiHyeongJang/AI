# 개발 환경
     OS : window10 PC
     Graphics Card : RTX 3080

# 도커
      Docker version : 20.10.21, build baeda1f
      CONTAINER Name : jsh
       : 아나콘다, cuda11.2, cudnn8.1, tensorflow=2.10.0


# Coding
1. 클린코드 관련
2. Process & Thread 폴더 - 파이썬 멀티 프로세싱 (함수 FOR문 돌리기 - multiprocessing 라이브러리 - pool 활용)
3. Dynamic Programming
4. sourcedefender (암호화 라이브러리)

[999] 간단하게 사용할 수 있는 코딩 : String to Datetime, 인자전달받기, 하위폴더탐색

# AI
## Images
1. stable-diffusion-tensorflow : 도커 환경을 통한 stable-diffusion 테스트 및 구현
2. Tesseract-OCR : 이미지 캡쳐 후 번역하기 (기능 : 전체화면 번역, 선택창 번역(선택하고R클릭), 범위 번역 (R~R-R클릭범위))
 -캡쳐 후 번역 프로그램 만들기 <Image 활용 (이미지 생성) -> Tesseract-OCR 활용 - 설치필요  (OCR : 이미지-> 영어 추출) -> googletrans 라이브러리 (구글 번역 : 영어-> 한글) -> tkinter 라이브러리 (GUI 구성)>
 3. 숫자 인식(사진 -> 동영상 딜미터기 만들어보기 - 계획중)
999. GDXRAY : 스마트 팩토리 관련 구현 확인(해당 GitHub 중단됨)

## NLP
1. KoBERT 학습 -> KorQuAD 2.0 도전

## Model
1. Logistic regression

## DB
1. MongoDB : UTC, KST 쉽게 Select하는 패키지 만들기,sourcedefender 라이브러리(암호화)
2. PostgreSQL : DB연결 및 BETWEEN, 현재 상태 값 테이블 로직
3. HIVE : DB연결 및 SELECT
4. ORACLE : 시노님관련 이슈 해결

# Python
- 3.5 : type hint (typing ,mypy)
- 3.11.0b4 : Faster CPython : 이전 버전에 비해 (3.10) 전반적인 실행 속도가 10%~60% 정도, 평균적으로는 25% 정도 빨라짐
 -> https://www.python.org/downloads/release/python-3110b4/
