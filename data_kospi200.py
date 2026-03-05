"""
kospi 200을 돌면서 데이터 수집 및 csv 저장
"""

import pandas as pd
import FinanceDataReader as fdr

def get_price_data(stock_code:str):
    """
    stock_code에 해당하는 주식의 주가 데이터 수집하여 csv로 저장
    """
    price_df = fdr.DataReader(stock_code)
    price_df.to_csv(f"data/{stock_code}.csv", encoding="utf-8-sig")

def get_kospi_200():
    """
    KOSPI 200 주식을 하나씩 돌면서 주가 데이터 수집
    """
    df_kospi = fdr.StockListing('KOSPI')
    
    # 2. 시가총액(Marcap) 기준 내림차순 정렬 후 상위 200개 선택
    kospi200_list = df_kospi.sort_values(by='Marcap', ascending=False).head(200)
    
    # 3. 필요한 정보(종목코드, 종목명)만 추출
    # fdr에서 코드는 'Code' 컬럼에 있습니다.
    return kospi200_list[['Code', 'Name']]

get_kospi_200()