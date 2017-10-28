import argparse
import csv

parser = argparse.ArgumentParser(description='Yodobashi Gold Point card csv to Moneyforward csv')
parser.add_argument('yodobashi_csv_path')
args = parser.parse_args()

yodobashi_csv_path = args.yodobashi_csv_path

print('Reading ' + yodobashi_csv_path + '...')

with open(yodobashi_csv_path, 'r', encoding='shift_jis') as f:
    mf_csv_filename = yodobashi_csv_path.replace('.csv', '_mf.csv')

    reader = csv.reader(f)
    writer = csv.writer(open(mf_csv_filename, 'w'))

    # write header
    writer.writerow(['計算対象', '日付', '内容', '金額（円）', '保有金融機関', '大項目', '中項目', 'メモ', '振替', 'ID'])

    for row in reader:
        newRow = []
        newRow.append('')
        newRow.append(row[0])
        newRow.append(row[1])
        newRow.append('-' + row[6])
        newRow.append('ヨドバシゴールドポイントカード')
        newRow.append('')
        newRow.append('')
        newRow.append('')
        newRow.append('')
        newRow.append('')

        writer.writerow(newRow)
