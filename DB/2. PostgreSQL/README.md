# 커넥션
## select to DataFrame

        connection = psycopg2.connect("host=ip dbname=k user=k password=pw port=숫자포트")
                cur = connection.cursor()
                # 쿼리 날리기
                cur.execute(sql2)
                rows=cur.fetchall()
                rbt_lbl=pd.DataFrame(rows)
        connection.close()


## 아래와 같이 정의 between A and B (범위 A(작은범위)~B(큰범위 )
파이썬에서 interval로 날리면 인식 못 하는점 있는것 같음

        sql3_3='select * from k.public."테이블명" where "타겟날짜" between {condition1}::timestamp and {condition3}::timestamp '.format(
        condition1 = "'"+[날짜등등]+"'",
        condition3 ="'"+[날짜등등].strftime('%Y-%m-%d %H:%M:%S')+"'" )


# INSERT

     engine = create_engine("postgresql://user:pw@IP:PORT/k")
        df.to_sql(name = 'F_PRDCN_STS',
                  con = engine,
                  schema = 'public',
                  if_exists = 'append',
                  index = False
                  )             
    except Exception as e:    
        print('save_P_DN8_STATUS 에러 발생 코드 :', e)
        
    finally:
        engine.dispose()  

# 그룹별로 top N개 가져오기

     with ab as (
        SELECT substring("EXCTN_YMDHM"::VARCHAR,1,10) as date -- 그룹화할 컬럼
        ,"MNF_SN", 
               ROW_NUMBER() OVER (PARTITION BY substring("EXCTN_YMDHM"::VARCHAR,1,10) ORDER BY "MNF_SN"  DESC) as ranking --ROW 그룹화함
        FROM public."P_MNFGDS_BDNS"
        where "BDNS_FRCST_TYPE" = '1'
        )
        select ab.date,ab."MNF_SN"
        from ab
        where ab.ranking<= 5 -- 5개 까지

# 그룹별 random 값 UPDATE

        UPDATE 
        public."P_MNFGDS_BDNS" -- 테이블명
        set
        "BDNS_PRBLTY" = 80+10*random()  -- UPDATE 컬럼 = 값
        where (substring("EXCTN_YMDHM"::VARCHAR,1,10),"MNF_SN") in ( -- "EXCTN~"그룹으로 조회, 날짜
        with ab as (
        SELECT substring("EXCTN_YMDHM"::VARCHAR,1,10) as date
        ,"MNF_SN", 
               ROW_NUMBER() OVER (PARTITION BY substring("EXCTN_YMDHM"::VARCHAR,1,10) ORDER BY "MNF_SN"  ASC) as ranking 
        FROM public."P_MNFGDS_BDNS"
        where "BDNS_FRCST_TYPE" = '1'
        )
        select ab.date,ab."MNF_SN"
        from ab
        where ab.ranking BETWEEN '89' and '90' -- TOP ROW 조건
        )
        and "BDNS_FRCST_TYPE" ='6' -- 마지막 필터 조건


# 쿼리 날리기 - 현재 상태를 가지고 있는 테이블 정의
## 현재 상태(max값)를 제외한 데이터 제거, update 기준 정의

### ETL 시 HH12, HH24 잘 써야 데이터 정합성에서 문제가 안 생김
