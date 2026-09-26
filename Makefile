# Python 과제의 실행·테스트·측정을 한 단어로 돌린다.

.PHONY: all run test bench charts clean

all: test

run:
	@python3 src/main.py

test:
	@python3 -m unittest discover -s tests -v

bench:
	@mkdir -p report
	@python3 tools/benchmark.py > report/results.csv
	@echo "wrote report/results.csv"

charts: report/results.csv tools/chart.py
	@python3 tools/chart.py
	@echo "wrote report/time_*.svg"

clean:
	rm -rf src/__pycache__ tests/__pycache__ tools/__pycache__
