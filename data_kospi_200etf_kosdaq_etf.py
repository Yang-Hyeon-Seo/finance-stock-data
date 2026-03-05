"""
목표
1. 데이터 수집 - 라이브러리 이용
2. KOSPI 200 종목을 돌면서 기술적 분석
3. AI 및 뉴스 분석을 통해 현재 가격이 합리적인건지 비합리적인건지(투기성/변동성) 파악
4. 변동성이 큰 주식과 변동성이 작은 주식들을 기준으로 안정성을 상/중/하로 구분하여 사용자의 위험 선호도에 따른 주식 추천
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import FinanceDataReader as fdr
import os

# 데이터 수집
"""
크롤링보다는 네이버 증권 데이터를 쉽게 가져올 수 있는 라이브러리 활용
pykrx
finance-datareader
"""
def fdr_kodex200etf_kodexkosdaqetf():
    """
    KODEX 200 ETF와 KODEX 코스닥 ETF 수정 종가 불러와서
    그래프로 그리고
    표로 출력
    KODEX 200 ETF 코드 : 069500
    """
    price_df = fdr.DataReader('069500, 229200')
    # fdr의 DataReader의 결과는 pandas df 형태임
    
    # 그래프 출력
    # sns.set_style('whitegrid')
    # price_df.plot()
    # plt.show()

    kodex200etf_price_df = fdr.DataReader('069500')
    # print(kodex200etf_price_df)

    kodexkosdaqetf_price_df = fdr.DataReader('229200')

    kodex200etf_price_df.to_csv('kodex200etf_price.csv', encoding='utf-8-sig')
    kodexkosdaqetf_price_df.to_csv('kosdaqetf_price.csv', encoding='utf-8-sig')

fdr_kodex200etf_kodexkosdaqetf()