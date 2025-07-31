#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
將 observation.ipynb 中的測站資料轉換為 CSV 格式
"""

import pandas as pd
import re
import json
from pathlib import Path

def parse_observation_data(file_path):
    """解析 observation.ipynb 檔案中的測站資料"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 嘗試解析為 JSON 格式的 Jupyter Notebook
    try:
        notebook = json.loads(content)
        # 提取所有 cell 的內容
        all_text = ""
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                for output in cell.get('outputs', []):
                    if 'text' in output:
                        all_text += '\n'.join(output['text'])
            elif cell.get('cell_type') == 'markdown':
                all_text += '\n'.join(cell.get('source', []))
    except json.JSONDecodeError:
        # 如果不是標準 JSON 格式，直接讀取文字
        all_text = content
    
    # 尋找表格資料
    lines = all_text.split('\n')
    
    # 找到表格開始的位置
    table_start = None
    for i, line in enumerate(lines):
        if '站號\t站名\t站種' in line:
            table_start = i
            break
    
    if table_start is None:
        # 如果找不到標準格式，嘗試尋找其他可能的標題行
        for i, line in enumerate(lines):
            if '站號' in line and '站名' in line and '站種' in line:
                table_start = i
                break
    
    if table_start is None:
        raise ValueError("找不到表格標題行")
    
    # 提取表格資料
    table_data = []
    for line in lines[table_start:]:
        # 跳過空行和標題行
        if line.strip() == '' or '站號\t站名\t站種' in line:
            continue
        
        # 檢查是否到達表格結束（遇到新的標題或空行）
        if line.startswith('二、已撤銷測站') or line.startswith('站號\t站名\t站種'):
            break
        
        # 解析表格行 - 處理 JSON 字串格式
        if '\t' in line:
            # 移除可能的 JSON 包裝
            clean_line = line.strip()
            if clean_line.startswith('"') and clean_line.endswith('",'):
                clean_line = clean_line[1:-2]  # 移除開頭的 " 和結尾的 ",
            elif clean_line.startswith('"') and clean_line.endswith('"'):
                clean_line = clean_line[1:-1]  # 移除開頭的 " 和結尾的 "
            
            # 處理轉義字符
            clean_line = clean_line.replace('\\t', '\t').replace('\\n', '\n')
            
            if '\t' in clean_line:
                table_data.append(clean_line)
    
    # 定義欄位名稱
    columns = ['站號', '站名', '站種', '海拔高度(m)', '經度', '緯度', '城市', '地址', 
               '資料起始日期', '撤站日期', '備註', '原站號', '新站號']
    
    # 解析資料
    parsed_data = []
    for row in table_data:
        if row.strip():
            # 分割欄位
            fields = row.split('\t')
            
            # 確保欄位數量正確
            if len(fields) >= 13:
                parsed_data.append(fields[:13])
            elif len(fields) > 0:
                # 如果欄位不足，用空字串填充
                fields.extend([''] * (13 - len(fields)))
                parsed_data.append(fields[:13])
    
    # 建立 DataFrame
    df = pd.DataFrame(parsed_data, columns=columns)
    
    return df

def main():
    """主函數"""
    # 讀取 observation.ipynb 檔案
    observation_file = 'observation.ipynb'
    
    try:
        # 解析測站資料
        df = parse_observation_data(observation_file)
        
        print(f"成功解析 {len(df)} 筆測站資料")
        print("\n前 5 筆資料:")
        print(df.head())
        
        # 儲存為 CSV 檔案
        output_file = 'observation_stations.csv'
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        print(f"\n資料已儲存至 {output_file}")
        
        # 顯示資料統計資訊
        print("\n資料統計:")
        print(f"總測站數: {len(df)}")
        print(f"欄位數: {len(df.columns)}")
        print("\n欄位名稱:")
        for i, col in enumerate(df.columns, 1):
            print(f"{i}. {col}")
        
        print("\n站種統計:")
        print(df['站種'].value_counts())
        
    except Exception as e:
        print(f"處理檔案時發生錯誤: {e}")

if __name__ == "__main__":
    main() 