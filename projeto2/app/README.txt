Flask

https://www.youtube.com/watch?v=r40pC9kyoj0

Micro Framework python feito para web

Ferramenta para simplificar o desenvolvimento WEB

site: flask.pocoo.org

instalar 
$pip install Flask 

Instalar o Virtualenv
$pip install virtualenv

Criar o projeto 
$ virtualenv venv 

Executar o ambiente virtual
$ . venv/bin/activate

Instalar o flask dentro do venv
$pip install flask

Verificar o que está instalado no ambiente virtual
$ venv/bin/pip freeze
click==6.7
Flask==1.0.2
freeze==1.0.10
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
six==1.11.0
Werkzeug==0.14.1

Salvar as informações em um arquivo .txt
$ venv/bin/pip freeze > requirements.txt

Instalar as dependencias a partir do requirements
$ venv/bin/pip install -r requirements.txt


Padra organização MVC

MODEL => Banco de dados - Informações

VIEW => O que o usuário vê

CONTROLER => Parte lógica


Flask SQLAlchemy

Banco de dados

Instalar o flask-sqlalchemy
$ venv/bin/pip install flask-sqlalchemy

Migração do Banco de dados - Sempre que for feita alguma alteração no DB

Instalar o flask-migrate e o flas-Script

$ venv/bin/pip install flask-migrate
$ venv/bin/pip install flask-script

Fazer a importação do Banco de dados
$ python run.py runserver

Para inicializar o DB
$ python run.py db init

Para fazer a migração do BD
$ python run.py db migrate

Para fazer o upgrade do BD
$ python run.py db upgrade

Instalando o Flask WTF
Gerenciador de formulário
$venv/bin/pip install flask-wtf








