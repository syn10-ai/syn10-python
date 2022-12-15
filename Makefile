.PHONY: build install

build:
	python -m build

install:
	python -m pip install .