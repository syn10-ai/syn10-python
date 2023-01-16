.PHONY: build install all

all: build install

build:
	python -m build

install:
	python -m pip install .

clean:
	rm -rf build dist *.egg-info .pytest_cache