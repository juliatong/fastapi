# Makefile for Docker Compose project

# Variables
DOCKER_COMPOSE = docker-compose
APP_SERVICE = api
DB_SERVICE = db

# Targets
install:
	@echo "Installing Docker Compose project dependencies..."

build:
	@echo "Building Docker Compose project..."
	$(DOCKER_COMPOSE) build

up:
	@echo "Starting Docker Compose services..."
	$(DOCKER_COMPOSE) up -d

down:
	@echo "Stopping Docker Compose services..."
	$(DOCKER_COMPOSE) down

view:
	@echo "Viewing Docker Compose services..."
	$(DOCKER_COMPOSE) ps

logs:
	@echo "Showing Docker Compose logs..."
	$(DOCKER_COMPOSE) logs -f


test: 
	@echo "Running all the tests..."
	pyest

restart: down up

shell-app:
	@echo "Starting a shell inside the app container..."
	$(DOCKER_COMPOSE) exec -it $(APP_SERVICE) /bin/bash

shell-db:
	@echo "Starting a shell inside the database container..."
	$(DOCKER_COMPOSE) exec -it $(DB_SERVICE) /bin/bash

set-up
	@echo "Setting up projetcs..."
	python create_tables.py

deploy: install build up view
setup: shell-app set-up
test: shell-app test

.PHONY: install build up down logs restart shell-app shell-db deploy test set-up
