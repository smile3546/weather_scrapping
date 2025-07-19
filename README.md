# 中央氣象署 CODiS 測站資料爬取工具

## 專案概述

這是一個用於批次下載中央氣象署 CODiS（Climate Observation Data Information System）測站資料的 Python 工具。該工具可以自動化下載指定日期範圍內的氣象觀測資料，並將結果保存為 JSON 格式。

## 功能特色

- 🔄 **批次下載**：支援指定日期範圍的批次資料下載
- 📊 **資料格式**：將氣象資料保存為結構化的 JSON 格式
- ⏱️ **進度顯示**：使用 tqdm 顯示下載進度
- 🛡️ **錯誤處理**：具備完善的錯誤處理機制
- 🌐 **API 整合**：直接整合中央氣象署 CODiS API
- 📅 **時間範圍**：預設下載 2016-04-29 至 2025-07-16 的資料

## 安裝需求

### 系統需求
- Python 3.7 或更高版本
- 網路連線

### 套件安裝

```bash
pip install requests tqdm
```

## 使用方法

### 基本使用

1. **執行 Jupyter Notebook**
   ```bash
   jupyter notebook 桃山scrapping.ipynb
   ```

2. **或直接執行 Python 腳本**
   ```bash
   python -c "$(cat 桃山scrapping.ipynb | jq -r '.cells[0].source[]')"
   ```

### 輸出檔案

程式執行完成後會產生：
- `codis_C0F9Y0_20160429_20250716.json`：包含所有下載資料的 JSON 檔案

## 程式碼結構

### 主要功能模組

- **`daterange()`**：產生日期範圍迭代器
- **`build_payload()`**：根據日期建立 API 請求參數
- **`fetch_day()`**：向 CODiS 伺服器請求單日資料
- **`save_results()`**：將結果保存為 JSON 檔案
- **`main()`**：主要執行流程

### 設定參數

```python
API_URL = "https://codis.cwa.gov.tw/api/station?"
STN_ID = "C0F9Y0"     # 測站 ID
STN_TYPE = "auto_C0"  # 測站類型
UTC_OFFSET = "+08:00"  # 台灣時區
```

## 資料來源

- **API 端點**：中央氣象署 CODiS 系統
- **測站資訊**：C0F9Y0 自動測站
- **資料類型**：氣象觀測報告

## 注意事項

### 使用限制
- 請遵守中央氣象署的使用條款
- 建議在非尖峰時段執行，避免對伺服器造成過大負載
- 程式內建 0.2 秒的請求間隔，確保禮貌性存取

### 錯誤處理
- 程式會自動處理網路連線錯誤
- 失敗的日期會記錄警告訊息，但不中斷整體執行
- 建議在穩定的網路環境下執行

## 輸出格式

JSON 檔案包含以下結構：
```json
[
  {
    "query_date": "2016-04-29",
    "data": {
      // 氣象觀測資料
    }
  }
]
```

## 開發環境

- **語言**：Python 3
- **主要套件**：requests, tqdm
- **開發工具**：Jupyter Notebook

## 授權

本專案僅供學習和研究使用，請遵守相關資料來源的使用條款。

## 聯絡資訊

如有問題或建議，請透過 GitHub Issues 提出。

---

**⚠️ 免責聲明**：本工具僅供學術研究使用，使用者需自行承擔使用風險，並遵守相關法規和資料來源的使用條款。 