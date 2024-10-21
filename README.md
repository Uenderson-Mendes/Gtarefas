

# Tarefas App

Este projeto é uma aplicação Django para gerenciar tarefas.

## Configuração do Ambiente

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd nome-do-repositorio
```

### 2. Crie o ambiente virtual:
```bash
virtualenv venv
```

### 3. Ative o ambiente virtual:

#### Linux/MacOS:
```bash
source venv/bin/activate
```

#### Windows:
```bash
venv\Scripts\activate
```

### 4. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 5. Execute as migrações:
```bash
python manage.py makemigrations tarefas
python manage.py migrate
```

### 6. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor:
```bash
python manage.py runserver
```

Acesse o app em `http://127.0.0.1:8000/`.


