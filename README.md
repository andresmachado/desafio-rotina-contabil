# desafio-rotina-contabil

Desafio: criar um CRUD o model Fluxograma:
OBS: Qualquer pacote do PyPI é permitido. Exemplo: django-widget-tweaks

### 1 - Criar um projeto
* Criar um projeto Django (criar um app e usar sqlite3)
* Usar o models.py fornecido. Adições são permitidas, mas não é permitido alterar os relacionamentos.

### 2 - Create
* Criar uma View onde é possível criar um Fluxograma.
* O usuário deve ser capaz de criar Tarefas (Apenas digitando o título). O usuário **não deve ser redirecionado** para outra view. Ajax é permitido.
* O usuário deve ser capaz de ordenar as tarefas. Recomendamos usar este componente: http://jqueryui.com/sortable/
* URL: localhost:8000/fluxograma/create

### 3 - Update
* Criar uma View que permita o Update do Fluxograma. (Considerando criação e ordenação de tarefas)
* URL: localhost:8000/fluxograma/pk/update

### 4 - Detail
* Criar uma View que mostre a ordem das tarefas de um fluxograma.
* URL: localhost:8000/fluxograma/pk
