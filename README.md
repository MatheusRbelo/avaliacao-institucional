# Mini Avaliação Institucional

## Como rodar

```bash
git clone https://github.com/MatheusRbelo/avaliacao-institucional.git
cd avaliacao-institucional/backend

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

O banco (`db.sqlite3`) não vai para o repositório, então quem clonar começa com o
banco vazio: é preciso rodar o `migrate`, criar o superusuário e cadastrar os
dados pelo Admin em http://127.0.0.1:8000/admin/.

## Respostas

### 1. Por que usar um ambiente virtual em cada projeto?

Cada projeto pode precisar de versões diferentes das mesmas bibliotecas (ex.: Django 4 em um, Django 6 em outro). O venv cria um espaço isolado para cada projeto, então um não quebra o outro. Como o venv só tem o que o projeto usa, o `pip freeze` gera um `requirements.txt` limpo, e qualquer pessoa consegue recriar o mesmo ambiente.

### 2. Por que dividir o sistema em 3 apps em vez de um só?

Cada app cuida de um assunto, o que facilita encontrar e corrigir as coisas (problema de aluno → pasta `alunos/`). A divisão também deixa clara a dependência: `avaliacoes` usa `alunos` e `disciplinas`, mas esses dois não dependem de ninguém. Assim dá para mexer em uma parte sem quebrar outra e até reaproveitar um app em outro projeto.

### 3. Para que servem `makemigrations` e `migrate`, e por que nessa ordem?

O `makemigrations` compara os `models.py` com o estado anterior e gera um arquivo com as mudanças necessárias, sem mexer no banco. O `migrate` aplica esses arquivos no banco de verdade e registra o que já foi executado. A ordem importa porque o `migrate` só aplica o que já foi gerado: primeiro se escreve a receita, depois se executa.
