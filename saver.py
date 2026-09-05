# save.py
import csv
import json
import os

def save_to_csv(records, filename):
    """
    将记录列表保存为 CSV 文件（UTF-8 with BOM，兼容 Excel）
    """
    if not records:
        print('未存储数据，无法生成CSV文件！')
        return
    try:
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f1:
            writer = csv.DictWriter(f1, fieldnames=['页面', '标题', '日期', '详情链接'])
            writer.writeheader()
            writer.writerows(records)
            print(f'CSV已保存！共 {len(records)} 条记录')
    except Exception as e:
        print(f' 保存 CSV 失败：{e}')

def save_to_json(records, filename='results.json'):
    """
    将记录列表保存为 JSON 文件（格式化，支持中文）
    """
    if not records:
        print('未储存数据，无法生成JSON文件！')
        return
    try:
        with open(filename, 'w', encoding='utf-8') as f2:
            json.dump(records, f2, ensure_ascii=False, indent=2)
        print(f'JSON已保存！共 {len(records)} 条记录')
    except Exception as e:
        print(f' 保存 JSON 失败：{e}')

def save_all(records, csv_file, json_file):
    """
    同时保存为 CSV 和 JSON，并打印文件绝对路径
    """
    save_to_csv(records, csv_file)
    save_to_json(records, json_file)
    # 打印文件位置
    print(f'CSV 文件位置：{os.path.abspath(csv_file)}')
    print(f'JSON 文件位置：{os.path.abspath(json_file)}')