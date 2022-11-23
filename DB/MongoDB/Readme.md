파이썬 pye 패키지

UTC 시간으로 load 되어서 패키지 어떻게 만드는지 공부하는겸 만든 파일

pye 파일이며, 암호화 되어있음. 암호화 패키지를 사용하려다가 pye 파일로 사용하려고 sourcedefender 패키지 사용
import sourcedefender 후에 패키지 로드해야지 사용 가능.

현재 버전 v1

사용법은 html 파일 참고, 오타 있을 수 있음.

나중에 추가해볼 내용, 매서드? 검색시 도움말 표시

기능

클래스 선언과 동시에 connect 후 매서드 사용
매서드명 : 기능
1. search_all : 해당 테이블 전체 조회 (날짜값 UTC)
2. search_all_timezone_convert : 해당 테이블 전체 조회 (날짜값 KST)
3. search_col_up : 해당 테이블 컬럼 1개 기준 날짜 이상 값들 조회 (날짜값 UTC)
4. search_col_between : 해당 테이블 컬럼 1개 기준 날짜 Between 값들 조회 (날짜값 UTC)
5. search_col_up_timezone_convert_kst : 해당 테이블 컬럼 1개 기준 날짜 이상 값들 조회 (날짜값 KST)
6. search_col_timezone_convert_between : 해당 테이블 컬럼 1개 기준 날짜 Between 값들 조회 (날짜값 KST)

