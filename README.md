# 개발 환경
     OS : window10 PC
     Graphics Card : RTX 3080

# 도커
      Docker version : 20.10.21, build baeda1f
      CONTAINER Name : jsh
       : 아나콘다, cuda11.2, cudnn8.1, tensorflow=2.10.0
       : pyspark Test(postgreSql)

# 도커(Airflow)
      Airflow compose up을 사용함 
      참고url  :https://it-is-my-life.tistory.com/21
       : url에서는 입맛대로 바꾸기 힘들어서 새로 추가함 port 설정이나 airflow 컨테이너가 여러개 나눠져있어서, 패키지 설치시 문제점이 발생함
       : 만든 부분에 대한 장점, Airflow 한 도커로 통일로 쉽게 패키지 설치 가능,  추후 pip install -r 을 통해서 쉽게 관리 가능할 것으로 보임. PostgresqlDB 또한 컨테이너를 통해서 연동시켜둠
       
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
1. KoBERT 학습 -> KorQuAD 2.0 공부해서 준비중

## Model
1. Logistic regression

## DB
1. MongoDB : UTC, KST 쉽게 Select하는 패키지 만들기,sourcedefender 라이브러리(암호화)
2. PostgreSQL : DB연결 및 BETWEEN, 현재 상태 값 테이블 로직, pyspark
3. HIVE : DB연결 및 SELECT
4. ORACLE : 시노님관련 이슈 해결

## openAPI
1. LoskArk API 활용하기

# Python
## Coding Convention (PEB8)
### Code lay-out
- 들여쓰기는 공백 4칸을 권장(아직 텝이 편함)
- 한 줄은 최대 79자까지 작성
- 최상위(top-level) 함수와 클래스 정의는 2줄씩 띄어 쓰기
- 클래스 내의 메소드 정의는 1줄씩 띄어 쓰기
### Code lay-out
- 불필요한 공백 제거
     - ([]) (()) 안
     - 쉼포, 쌍점: 쌍반점; 앞
- 키워드 인자(keyword argument)와 인자의 기본값(default parameter value)의 = 붙여 쓰기

추가작성중
#### Jupyter
셀 삭제 복구 : ESC + Z
## 다른 이슈
- 3.5 : type hint (typing ,mypy)
- 3.11.0b4 : Faster CPython : 이전 버전에 비해 (3.10) 전반적인 실행 속도가 10%~60% 정도, 평균적으로는 25% 정도 빨라짐
 -> https://www.python.org/downloads/release/python-3110b4/
