# chatbot
## はじめに
これは http://sandmark.hateblo.jp/entry/2017/10/07/141339 を基に作成したchatbot(人工無能)である．

## Information
### dictionary.py
パターン，テンプレート，ランダム，マルコフ辞書に関するファイル
### main.py
このファイルを動かすことによりチャットボットを起動させることが出来る
```
python main.py
```
### markov.py
マルコフ連鎖による文章の学習・生成を行う．

外部の文章を学習させると賢くなる．(かも)

青空文庫(https://www.aozora.gr.jp/index_pages/person_all.html )から学習させるときはtext_preprocessing.pyを使うと便利

文章を学習させる方法は以下の通り．
```
python markov.py hoge.txt
```
### morph.py
形態素解析を行う
### responder.py
ユーザーの入力に対する応答を行う
### text_preprocessing.py
青空文庫(https://www.aozora.gr.jp/index_pages/person_all.html )からダウンロードした文章をmarkov.pyが学習しやすい形に整形する
### unmo.py
応答方式の決定，辞書への保存を行う
### util.py
エラー内容を出力する
