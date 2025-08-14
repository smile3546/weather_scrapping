# 氣象資料爬取與處理專案

## 專案說明
這個專案用於從中央氣象署的 CODIS 系統爬取氣象站資料，並進行資料清理處理。

## 檔案結構

### 主要程式檔案
- weather_scrapping.ipynb: 主要的氣象資料爬取程式
- clean_weather_csv.ipynb: 資料清理與處理程式
- weather_scrapping_origin.ipynb: 原始的單一氣象站爬取程式

### 資料檔案
- csv/mountain_two_simple.csv: 山峰與對應氣象站資訊
- csv/mountain_lanlon.csv: 山峰經緯度資訊
- csv/observation_stations.csv: 氣象站資訊
- weather_csv/: 原始爬取的氣象資料
- clean_weather_csv/: 清理後的氣象資料

## 使用方式

### 步驟一：爬取氣象資料
執行 weather_scrapping.ipynb
- 讀取 mountain_two_simple.csv 中的氣象站編號
- 自動去除重複的站號
- 爬取 2016-04-29 到 2025-08-14 的氣象資料
- 每次請求限制 30 天資料量
- 輸出檔案格式：{站號}_weather.csv

### 步驟二：資料清理
執行 clean_weather_csv.ipynb
- 解析原始 JSON 格式資料
- 提取關鍵欄位：StationID、DataTime、AirTemperature、RelativeHumidity、Precipitation
- 將小於 -50 的異常值設為空值
- 輸出清理後的 CSV 檔案

## 資料說明

### 原始資料來源
中央氣象署 CODIS 系統 API
網址：https://codis.cwa.gov.tw/api/station

### 處理後資料欄位
- StationID: 氣象站編號
- DataTime: 觀測時間
- AirTemperature: 氣溫（攝氏度）
- RelativeHumidity: 相對濕度（百分比）
- Precipitation: 降雨量（毫米）

### 資料時間範圍
2016年4月29日 至 2025年8月14日

### 涵蓋氣象站
依據 mountain_two_simple.csv 中記錄的山峰最近氣象站，包含17個不重複的氣象站編號

## 注意事項
- API 每次請求限制最多 31 天資料
- 異常值（小於 -50）已被設定為空值
- 部分氣象站可能因設備故障造成資料缺失
- 資料僅供研究與分析使用
