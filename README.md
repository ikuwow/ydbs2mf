# ydbs2mf

Converts Yodobashi gold point card csv to Moneyforward csv

## Usage


0. Go ["カードご利用明細紹介"](https://secure.goldpoint.co.jp/memx/web_meisai/top/index.html). (Needs login)
0. Select お支払い月 you need (bottom of the page)
0. Click "CSV形式で保存する" to download (filename is like `201710.csv`)
0. Run `ydbs2mf.py` script (generates `201710_mf.csv`)
0. Upload it to your account of Moneyforward (https://moneyforward.com/accounts/show/******)
0. Follow the instructions, done!

## How to run script

```
$ python ydbs2mf.py yodobashi.csv
```

It creates `yodobashi_mf.csv`.

## Requirements

Python 3

## License

MIT
