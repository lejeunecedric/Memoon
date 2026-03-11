.PHONY: help install dev run migrate createsuperuser test clean docker-build docker-run

help:
	@echo "Memoon - Content Structure Manager"
	@echo ""
	@echo "Available commands:"
	@echo "  make install          - Install dependencies with uv"
	@echo "  make dev             - Install dev dependencies"
	@echo "  make run             - Run development server on port 8089"
	@echo "  make migrate         - Apply database migrations"
	@echo "  make createsuperuser - Create admin user"
	@echo "  make test            - Run tests"
	@echo "  make clean           - Remove cache files"
	@echo "  make docker-build    - Build Docker image"
	@echo "  make docker-run      - Run Docker container"
	@echo "  make docker          - Build and run Docker"

install:
	uv sync

dev:
	uv sync --extra dev

run:
	python manage.py runserver 8089

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

collectstatic:
	python manage.py collectstatic --noinput

test:
	pytest

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

docker-build:
	docker build -t memoon:latest .

docker-run:
	docker run -d -p 8089:8089 --name memoon memoon:latest

docker: docker-build docker-run

logs:
	docker logs -f memoon

stop:
	docker stop memoon && docker rm memoon
