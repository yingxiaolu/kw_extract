import os.path
import sys
sys.path.append("./")
from lib.utils import dump_json


def load_text(fn):
    with open(fn, encoding="utf-8") as fin:
        return fin.read()


# stage 1: Try to locate Index/Glossary
# 思路：
# 先找到跟index/glossary匹配的段落，可能有多个，下面以Index距离
# 有些textbook的每页index（pdf页）都会有一个Index字样，它们在上面找到的段落相距应该不远
# 从后往前数Index标签对应的下标，一旦两个下标之间的差距大于阈值，则认为前一个Index是Index页面的第一页
# 举个例子：economics/game theory/目录下
# epistemic_game_theory.txt 是[13234, 13167, 13140], 应该取最后一个
# Algorithmic Game Theory by Noam Nisan, Tim Roughgarden, Eva Tardos, Vijay V_ Vazirani (z-lib_org).txt
# 是[20633, 20586, 20536, ..., 19983, 19936, 19886, 19848, 19822, 269]，应该取倒数第二个
def find_index_or_glossary_part(raw_text):
    # Potential Index or Glossary keywords
    kws = ["index", "indexes", "glossary", "glossaries"]
    paragraphs = raw_text.split("\n\n")
    index_marks = []
    for ind in range(len(paragraphs)-1, 0, -1):
        pg_content = paragraphs[ind]
        if pg_content.strip().lower() in kws:
            index_marks.append(ind)
    # print(index_marks)
    if len(index_marks) == 0:
        return ""
    gap = 100
    start_index = index_marks[0]
    for ind in index_marks:
        if start_index - ind <= gap:
            start_index = ind
        else:
            break
    return "\n\n".join(paragraphs[start_index:])


def process(fn):
    raw_text = load_text(fn)
    index_or_glossary_part = find_index_or_glossary_part(raw_text)
    return index_or_glossary_part


def batch_process():
    base_dir = "data/raw_data_textbook"
    index = 0
    for major in ["finance", "economics"]:
        major_dir = os.path.join(base_dir, major)
        for course in os.listdir(major_dir):
            course_dir = os.path.join(major_dir, course)
            for text_book in os.listdir(course_dir):
                if text_book.endswith(".txt"):
                    text_book_index_or_glossary = process(os.path.join(course_dir, text_book))
                    dump_json({"major": major, "course": course, "textbook": text_book, "index_glossary_part": text_book_index_or_glossary}, f"./data/textbook_index_glossary/{index}.json")
                    index += 1


if __name__ == '__main__':
    # process("./data/sample/sample_textbook.txt")
    batch_process()

