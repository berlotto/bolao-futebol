Bolão Futebol
=============

Software para bolão de futebol criado com Django e login social.


Características
---------------

- Focado em jogos de futebol
- Criação de grupos de bolão
- Login social via Facebook e Google
- Pode ser utilizado para quaisquer campeonatos
- Regras de pontuação conforme acertos na aposta:
    - __Placar exato__: 5 pts
    - __Acertar o vencedor, mas não o placar exato__: 4 pts
    - __Acertar o empate, mas não o placar exato__: 2 pts
    - __Não acertar nada__: 0 pts

Instalação
----------

- Faça o FORK do projeto

- Faça o clone do repositorio

      git clone https://github.com/<seu_user>/bolao-futebol.git

- Crie o virtualenv

        mkvirtualenv bolao

- Instale as dependencias

        pip install -r requirements.txt

- Configure em `settings.py` (se não for utilizar o Sqlite) e crie o banco

        python manage.py syncdb

- Rode o servidor

        python manage.py runserver

- Acesse a aplicação em : http://localhost:8000

- Depois, faça alterações de melhoria e submete um __Pull Request__ !

\o/



A fazer
-------

- Adicionar pagamento via PyPal para boloes pagos
- Fazer os pontos configuráveis
