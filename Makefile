install-debian:
	apt-get install htop python3-venv
	pip install -r requirements.txt

install-local:
	pip install -r requirements.txt

run:
	python benchmarks.py

build:
	docker build -t pybenchmarks .

publish:
	docker tag pybenchmarks moritzwilksch/infra-stuff:latest
	docker push moritzwilksch/infra-stuff:latest