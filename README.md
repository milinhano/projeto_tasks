# Sistema de Gerenciamento de Tarefas

## Sobre o projeto

Projeto didático desenvolvido na disciplina de Projeto de Desenvolvimento de Software, usando o framework **Django**. O sistema permite cadastrar e listar tarefas, com controle de usuários para login, logout e cadastro.

O projeto é dividido em dois aplicativos, cada um com uma responsabilidade própria:

| App | Responsabilidade |
|---|---|
| tarefas | Gerencia as tarefas: criar e listar |
| usuarios | Cuida da autenticação: login, logout e cadastro |

## Tecnologias utilizadas

- Python
- Django
- HTML e CSS
- JavaScript
- Bootstrap
- SQLite
- python-dotenv

## Estrutura do projeto

projeto_tasks/
├── venv/                 # Ambiente virtual (não vai para o GitHub)
├── manage.py
├── .env                  # Variáveis de ambiente (não vai para o GitHub)
├── .env.example          # Modelo do .env (vai para o GitHub)
├── .gitignore
├── requirements.txt
├── setup/                # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tarefas/              # App de tarefas
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── usuarios/             # App de usuários
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── templates/            # Arquivos HTML
│   ├── base.html
│   ├── tarefas/
│   └── usuarios/
└── static/               # CSS, JS e imagens

## Pré-requisitos

- Python instalado (versão 3.10 ou superior)
- Git instalado
- Conta no GitHub

## Como configurar o projeto na sua máquina

### 1. Clone o repositório
```bash
git clone https://github.com/usuario/projeto_tasks.git
cd projeto_tasks
```
O comando git clone baixa uma cópia completa do projeto para a sua máquina.

### 2. Crie o ambiente virtual
O ambiente virtual isola as dependências do projeto do resto do sistema:

```bash
python -m venv ./venv
```

Ative o ambiente. No Windows:

```bash
venv\Scripts\activate
```

No Linux ou Mac:
```bash
source venv/bin/activate
```

Quando ativar, o terminal passa a mostrar (venv) no início da linha.

### 3. Instale as dependências

O arquivo requirements.txt lista tudo o que o projeto precisa. Coma venv ativada execute:

```bash
pip install -r requirements.txt
```

Isso instala o Django e o python-dotenv de uma só vez.

### 4. Crie o arquivo .env

Copie o arquivo modelo e renomeie para .env:

```bash
cp .env.example .env
```

No Windows, se o comando cp não funcionar:

```bash
copy .env.example .env
```

Abra o .env. Ele contém:

```bash
CódigoSECRET_KEY=
DEBUG=True 
```

SECRET_KEY está vazia de propósito. Ela precisa ser gerada por cada pessoa, porque nunca é enviada para o GitHub.

### 5. Gere a sua SECRET_KEY

Com o ambiente ativado, execute:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

O terminal imprime uma chave aleatória, parecida com esta:

```bash
django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6
```

### 6. Cole a chave no .env

Copie a chave impressa e cole no arquivo, sem aspas e sem espaços:

```bash
SECRET_KEY=django-insecure-9x#k2$m4v@q7w8e9r1t2y3u4i5o6p7a8s9d0f1g2h3j4k5l6
DEBUG=True
```

Cada pessoa pode usar a sua própria chave. O projeto funciona normalmente com chaves diferentes, pois ela serve apenas para assinar sessões e cookies.

### 7. Crie o banco de dados

O arquivo db.sqlite3 também não vai para o GitHub. Cada máquina precisa criar o seu banco local:

```bash
python manage.py migrate
```

### 8. Rode o projeto

```bash
python manage.py runserver
```

Acesse http://localhost:8000/ no navegador.

## Como manter o projeto atualizado

Sempre comece o trabalho buscando as mudanças que os colegas enviaram:
```bash
git pull
```

Depois de alterar o código, envie as mudanças:

```bash
git add .
git commit -m "descrição do que foi feito"
git pull
git push
```

O git pull antes do git push evita conflitos: se alguém já enviou mudanças, o Git baixa e tenta juntar tudo.

| Erro | Causa | Solução |
|---|---|---|
| SECRET_KEY must not be empty | Arquivo .env não foi criado ou está vazio | Refazer os passos 4 a 6 |
| O comando manage.py não é reconhecido | Ambiente virtual não está ativado | Verificar se o terminal mostra (venv) no início da linha |
| Página 404 no navegador | URL digitada não corresponde a nenhuma rota | Conferir os caminhos no urls.py de cada app |