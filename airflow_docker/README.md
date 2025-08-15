# 개발 언어 
+ Python

# 개발환경정보
docker --version : Docker version 24.0.2, build cb74dfc <br/>
docker-compose --version : Docker Compose version v2.24.5 <br/>
lsb_release -a : Ubuntu 18.04.6 LTS<br/>

# 환경 구성
proj 폴더 - 5개의 폴더(컨테이너로 구성) <br/>
business_server(bns) : 비지니스 서버를 실행 Docker 외부 port : 9000 <br/>
detector_server(detector) : 디텍터 서버 Docker 외부port :7860 <br/>
captioner_server(captioner) : 캡셔너 서버 Docker 외부port :7788 <br/>
gpt_server(gpt2) : gpt2 서버 Docker 외부port :7789 <br/>
db(bns_db) : MySQL Docker 외부port :  3307 <br/>
db정보 등은 .env파일에 있음(+설정 정보 등) <br/>
각 컨테이너의 Dockerfile은 각 폴더의 Dockerfile을 사용 <br/>
패키지는 requirements.txt + Dockerfile 내에서 기입 (디펜던시 및 모델 동작 환경에 최적) <br/>
docker-compose.yml에서 각 서버들을 실행 app.py(이름은 각기 다를 수 있음) <br/>
 <br/>
+ 디텍팅서버에서 TEST -> 비지니스서버[ 디텍팅 모델 -> 캡셔닝 모델 -> gpt2 요약 ] -> db(MySQL)

# 간단한 분석 내용
detector 모델 중 ~ l 모델이 dog + bench로 유일하게 2개로 디텍팅 되었습니다. <br/>
-> 하지만, <br/>
captioner 모델만 썼을 경우  : a dog laying on top of a wooden bench <br/>
디텍팅 모델 -> 캡셔닝 모델의 output : black and white dog on ground <br/>
이렇게 나왔지만... 일단 디텍팅 모델 -> 캡셔닝 모델 -> gpt2 요약으로 진행했습니다. (각 서버의 옵션은 기본) <br/>

# 네트워크 정보
ip는 docker-compose 내부 ip로 동작할 수 있도록 구성 (임의로 172.88.0.0번대로 구성했는데 이미 ip가 있을 경우 변경할 필요가 있음) <br/>
port도 docker-compose.yml에 HOST:Docker 매핑을 임의적으로 해두었는데 중복시 변경해야함 <br/>
네트워크는 내부 네트워크를 사용하기 위해 아래와 같이 정의 <br/>
networks:  appnet <br/>
    driver: bridge <br/>
    name: appnet <br/>
    ipam: <br/>
      config: <br/>
        - subnet: 172.88.0.0/16 <br/>

# db관련
db : MySQL <br/>
table : appdb.jobs <br/>
컬럼 : <br/>
accepted : TINYINT(1)   NOT NULL DEFAULT 0   ## 즉시 응답의 Boolean(접수 성공 여부): /submit이 "ok": true면 1, 아니면 0 (Boolean)  <br/>
success : TINYINT(1)   NOT NULL DEFAULT 0  ## 최종 파이프라인 성공 여부(Boolean) <br/>
summary : 요약기능 <br/>
등등... <br/>


# 실행전 확인사항
IP, HOST_PORT, CONTAINER NAME 겹칠시 docker-compose.yml에서 수정이 필요함 <br/>

# 구동 순서
첨부된 proj 파일 압축해제 -> 리눅스 환경 + docker환경 <br/>
docker-compose up --build <br/>
(버전에 따라서 docker compose up --build) ## -d 옵션 등은 편하신대로하시면 됩니다. <br/>
테스트 실행전 확인 명령어 : curl -i http://172.88.0.10:9000 <br/>
-> 아래와 같이 나오면 테스트 진행 가능 <br/>
HTTP/1.1 200 OK <br/>
date: Fri, 15 Aug 2025 14:18:05 GMT <br/>
server: uvicorn <br/>
content-length: 60 <br/>
content-type: application/json <br/>
{"ok":true,"message":"Business Server up","version":"1.1.0"} <br/>
 <br/>
테스트는 detector 컨테이너에서 진행하도록 했습니다. <br/>
도커 진입 명령어 : docker exec -it detector bash <br/>
제공주신 이미지로 테스트 명령어 : python test_submit.py <br/> <br/>
추가로, 이미지 변경해서 테스트 원할시 : proj/detector_server/yolov12/image <- 이미지 파일 변경 <br/>

# 진행결과 확인
테스트 진행 결과는 db에 저장됩니다. 진행중인 내용도 MySQL로 확인 가능. <br/>
port : 3307 <br/>
db : appdb <br/>
id : appuser <br/>
pw : apppass <br/>
ip : host ip <br/>
