run:
	python manage.py runserver

sk:
	python generationSecureKey.py

ti:
	python manage.py makemigrations

te:
	python manage.py migrate

usr:
	python manage.py createsuperuser

migration:
	rm -rf API_Favorite_Products/migrations
	@echo "Migrações de banco excluídas"

db:
	rm -rf db.sqlite3
	@echo "banco excluído"


