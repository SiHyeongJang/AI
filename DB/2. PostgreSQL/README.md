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

# DB Insert 속도 개선 // Pandas DataFrame을 TSV 형식으로 메모리에 변환 (메모리 아웃 발생 방지, 속도 개선)

        from sqlalchemy import create_engine
        import psycopg2
        
        DB_HOST = import_data_config["host"]
        DB_PORT = import_data_config["port"]
        DB_NAME = import_data_config["dbname"]
        DB_USER = import_data_config["user"]
        DB_PASSWORD = import_data_config["password"]
        
        # PostgreSQL 연결 엔진 생성
        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        
        conn = engine.raw_connection()
        cursor = conn.cursor()
        
        # 청크 단위 설정
        chunk_size = 1_000_000
        
        # 청크로 나누어서 INSERT
        #스키마,테이블명,데이터프레임명 변경하여 사용 
        for i, chunk in enumerate(np.array_split(데이터프레임명, len(데이터프레임명) // chunk_size + 1)):
            output = io.StringIO()
            chunk.to_csv(output, sep='\t', header=False, index=False)
            output.seek(0)
            
            copy_sql = 'COPY "스키마"."테이블명" FROM STDIN WITH (FORMAT csv, DELIMITER E\'\\t\')'
            cursor.copy_expert(copy_sql, output)
            print(f"Chunk {i+1} inserted... ({len(chunk)} rows)")
        
        # 완료 처리
        conn.commit()
        cursor.close()
        conn.close()



# 추후 작성 예정 // 쿼리 날리기 - 현재 상태를 가지고 있는 테이블 정의
## 현재 상태(max값)를 제외한 데이터 제거, update 기준 정의

### ETL 시 HH12, HH24 잘 써야 데이터 정합성에서 문제가 안 생김
