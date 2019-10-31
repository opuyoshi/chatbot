# coding:'utf-8'
import sys
import zipfile
import re


def zip2ruby(fname):
    # retrieve textfile from zipfile
    with zipfile.ZipFile(fname, 'r') as zf:
        item = zf.infolist()[0]
        with zf.open(item.filename) as f:
            # テキストの文字コードのutf-8でデコードしておく
            return f.read().decode('shift-jis')


def ruby2text(ruby):
    # ルビなどの作品本文以外の文字や記号を取り除く
    txt = re.split(r'-{50,}', ruby)[2]
    txt = re.split(r'底本：', txt)[0]
    txt = re.sub(r'《.*？?》|[#.*?]|｜', '', txt)
    return txt.strip()


def main():
    argvs = sys.argv
    if len(argvs) != 2:
        print('Usage: python {} "zip file path" '.format(argvs[0]))
        exit()

    ruby = zip2ruby(argvs[1])
    txt = ruby2text(ruby)
    newfile = "new_neko.txt"
    with open(newfile, mode='w') as f:
        f.write(txt)
    # print(txt)


if __name__ == '__main__':
    main()
