
# Tarefas App

Este projeto é uma aplicação Django para gerenciar tarefas.

## Configuração do Ambiente

### 1. Clone o repositório:
```bash
git clone https://github.com/Uenderson-Mendes/Gtarefas.git
cd Gtarefas
```

### 2. Instale o `virtualenv` (caso não tenha instalado):
```bash
pip install virtualenv
```

### 3. Crie o ambiente virtual:
```bash
virtualenv venv
```

### 4. Ative o ambiente virtual:

#### Linux/MacOS:
```bash
source venv/bin/activate
```

#### Windows:
```bash
venv\Scripts\activate
```

### 5. Instale o Django e outras dependências:
```bash
pip install django

```

### 6. Execute as migrações:
```bash
python manage.py makemigrations tarefas
python manage.py migrate
```

### 7. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

### 8. Inicie o servidor:
```bash
python manage.py runserver
```

Acesse o app em `http://127.0.0.1:8000/`.

