b:
	docker compose -f docker-compose.prod.yml build
bud:
	docker compose -f docker-compose.prod.yml up -d --build
buddev:
	sudo docker compose -f docker-compose.dev.yml up -d --build

ud:
	docker compose -f docker-compose.prod.yml up -d

udev:
	docker compose -f docker-compose.dev.yml up -d

rdev:
	python manage.py runserver

u:
	docker compose -f docker-compose.prod.yml up
mm:
	docker exec -it django-clean-architecture-boilerplate-web-1 python manage.py makemigrations
vps_m:
	ssh chilime@173.212.218.196 'cd /home/chilime/django/chilime && docker exec -i django-clean-architecture-boilerplate-web-1 python manage.py migrate'
vps_m_merge:
	ssh chilime@173.212.218.196 'cd /home/chilime/django/chilime && docker exec -i django-clean-architecture-boilerplate-web-1 python manage.py makemigrations --merge'
m:
	docker exec -it django-clean-architecture-boilerplate-web-1 python manage.py migrate

cs:
	docker exec -it django-clean-architecture-boilerplate-web-1 python manage.py collectstatic --noinput

d:
	docker compose -f docker-compose.prod.yml down

ddev:
	docker compose -f docker-compose.dev.yml down

dv:
	docker compose -f docker-compose.prod.yml down -v

ddv:
	docker compose -f docker-compose.dev.yml down -v

sweb:
	docker exec -it django-clean-architecture-boilerplate-web-1 python manage.py shell

bweb:
	docker exec -it django-clean-architecture-boilerplate-web-1 bash

dweb:
	docker exec -it django-clean-architecture-boilerplate-db-1 bash

csu:
	docker exec -it django-clean-architecture-boilerplate-web-1 python manage.py createsuperuser
	docker exec -it django-clean-architecture-boilerplate-web-1 python manage.py createsuperuser

nrw:
	docker exec -it django-clean-architecture-boilerplate-web-1 npm run watch

nrp:
	docker exec -it django-clean-architecture-boilerplate-web-1 npm run production

ni:
	docker exec -it django-clean-architecture-boilerplate-web-1 npm install

lw:
	docker logs django-clean-architecture-boilerplate-web-1 -f

ld:
	docker logs django-clean-architecture-boilerplate-db-1

r:
	docker restart django-clean-architecture-boilerplate-web-1
	docker restart django-clean-architecture-boilerplate-db-1

rweb:
	docker restart django-clean-architecture-boilerplate-web-1
	docker exec -it django-clean-architecture-boilerplate-web-1 pip install -r dependencies/dev_requirements.txt
msg:
	docker exec -it django-clean-architecture-boilerplate-web-1  python manage.py makemessages

cmsg:
	docker exec -it django-clean-architecture-boilerplate-web-1  python manage.py compilemessages

idr:
	docker exec -it django-clean-architecture-boilerplate-web-1 pip install -r dependencies/dev_requirements.txt

iar:
	docker exec -it django-clean-architecture-boilerplate-web-1 pip install -r dependencies/apt_requirements.txt

dd:
	docker exec -t django-clean-architecture-boilerplate-db-1  pg_dump -c -U postgres > dump_data11.sql

dr:
	cat dump_data10.sql | sudo docker exec -i django-clean-architecture-boilerplate-db-1 psql -U postgres

cmd:
	docker exec -it django-clean-architecture-boilerplate-web-1 python manage.py commands


newdev:
	make buddev
	make dr

status:
	git status

push:
	git push origin

git:
	git add .
	git commit -m "$m"
	git push origin $b

fa:
	make cs
	make ni
	make nrp
	make nrtw

drs:
	rsync -avzP user@IP:/home/chilime/django/db_backups/dump_data10.sql chilime/
media_rsync:
     	rsync -avzP user@IP:/home/chilime/django/chilime/media chilime/