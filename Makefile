install:
	@pip install --upgrade pip
	@pip install poetry==1.1.12
	@poetry update
	@poetry shell
run:
	uvicorn main:app --reload

get:
	@curl -X GET http://localhost:8000/$(arg)