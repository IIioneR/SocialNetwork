
start_db:
	docker-compose -f stack.yml up

stop_db:
	docker-compose -f stack.yml down -v

migrate: 
	bash ./scripts/migrate.sh

run:
	bash ./scripts/run.sh

format:
	bash ./scripts/format.sh

