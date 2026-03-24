SHELL := /bin/bash
SPHINX := sphinx-build
BUILD_DIR := _build

# 日本語ビルド
ja:
	@echo "=== Building JA ==="
	cp docs/vars/ja.rst docs/vars/locale.rst
	SPHINX_LANG=ja $(SPHINX) -b html -D html_baseurl="/" . $(BUILD_DIR)/ja

# 英語ビルド
en:
	@echo "=== Building EN ==="
	cp docs/vars/en.rst docs/vars/locale.rst
	SPHINX_LANG=en $(SPHINX) -b html -D html_baseurl="/" . $(BUILD_DIR)/en

# クリーン
clean:
	rm -rf $(BUILD_DIR)