import requests, json, os.path, sqlalchemy, os, pymysql
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

# MySQL 연결
HOSTNAME = get_secret("Mysql_Hostname")
PORT = get_secret("Mysql_Port")
USERNAME = get_secret("Mysql_Username")
PASSWORD = get_secret("Mysql_Password")
DBNAME = get_secret("Mysql_DBname")

DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'
print('Connected to Mysql....')

engine = sqlalchemy.create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

class db_conn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connection()
        return conn


def healthCheck():
    return "OK"

def stock_data():
    url = 'https://apis.data.go.kr/1160100/service/GetStocDiviInfoService/getDiviInfo'
    params = '?serviceKey=' + get_secret("data_apiKey")
    params += '&pageNo=1&numOfRows=100&resultType=json'
    url += params
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        return data
    else:
        return None

def process_data(data):
    try:
        # API 응답 데이터 중에서 'items' 키에 해당하는 데이터 추출
        items = data['response']['body']['items']['item']
        
        # 필요한 데이터를 담을 리스트 초기화
        processed_data = []

        for item in items:
            # 필요한 데이터 추출 및 컬럼 이름 변경
            processed_item = {
                '기준일자': item['basDt'],
                '법인등록번호': item['crno'],
                '주식발행회사명': item['stckIssuCmpyNm'],
                '현금배당일자': item['cashDvdnPayDt'],
                'ISIN코드명': item['isinCdNm'],
                '주식배당사유': item['stckDvdnRcdNm'],
                '유가증권코드종류명': item['scrsItmsKcdNm'],
                '주식일반배당금액': item['stckGenrDvdnAmt'],
                '주식일반배당률': item['stckGenrDvdnRt'],
                '주식결산월일': item['stckStacMd']
            }
            processed_data.append(processed_item)
        
        return processed_data
    except KeyError:
        print("Invalid API response format.")
        return None

def insert_data_to_mysql(data):
    # 가공 없이 데이터를 그대로 DataFrame으로 변환
    df = pd.DataFrame(data)
    
    # MySQL 테이블에 데이터 삽입
    table_name = 'stock'
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print("Data inserted into MySQL table:", table_name)

def main():
    # 데이터 가져오기
    data = stock_data()
    if data:
        # 데이터 가공
        processed_data = process_data(data)
        
        # MySQL에 삽입
        insert_data_to_mysql(processed_data)
    else:
        print("Failed to fetch data from the API.")

def get_db_data():
    conn = engine.connect()
    metadata = MetaData()
    table_name = 'stock'
    table = Table(table_name, metadata, autoload_with=engine)
    stmt = select(table)
    results = conn.execute(stmt).fetchall()
    conn.close()

    # 쿼리 결과를 딕셔너리 형태로 변환
    data = [dict(zip(table.columns.keys(), result)) for result in results]

    return data

if __name__ == "__main__":
    main()

