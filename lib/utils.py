import docx2txt
import json


def dump_json(obj, fp, encoding='utf-8', indent=4, ensure_ascii=False):
    with open(fp, 'w', encoding=encoding) as fout:
        json.dump(obj, fout, indent=indent, ensure_ascii=ensure_ascii)


def load_json(fp, encoding='utf-8'):
    with open(fp, encoding=encoding) as fin:
        return json.load(fin)


def load_doc(fn):
    paragraphs = docx2txt.process(fn).split('\n')
    return paragraphs
