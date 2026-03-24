import re
from dataclasses import dataclass
import deepl


with open('./deepl.key') as f:
    key = f.read()
translator = deepl.Translator(key)
usage = translator.get_usage()


@dataclass
class SubstitutionText:
    name: str
    ja: str
    en: str|None

    def translate_if_needed(self):
        if self.en is not None:
            return self.en

        result = translator.translate_text(
            self.ja,
            source_lang='JA',
            target_lang='EN-US',
        )

        self.en = result.text
        return self.en


def parse_rst_substitutions(path):
    """
    ".. |var| replace:: テキスト" 形式の置換を抽出する簡易パーサ
    """
    pattern = re.compile(r"\.\.\s+\|(.+?)\|\s+replace::\s+(.*)")
    items = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = pattern.match(line)
            if m:
                var = m.group(1).strip()
                txt = m.group(2).strip()
                items[var] = txt

    return items


def main():
    ja_items = parse_rst_substitutions("ja.rst")
    en_items = parse_rst_substitutions("en.rst")

    substitutions = []

    for name, ja_text in ja_items.items():
        en_text = en_items.get(name)  # en.rst に無ければ None
        substitutions.append(SubstitutionText(name, ja_text, en_text))

    # 翻訳が必要なもののみ翻訳して en.rst に追記
    with open("en.rst", "a", encoding="utf-8") as f:
        for sub in substitutions:
            if sub.en_text is None:
                print(f"Translating: {sub.name}")
                translated = sub.translate_if_needed()
                f.write(f".. |{sub.name}| replace:: {translated}\n")


if __name__ == "__main__":
    main()