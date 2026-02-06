# SGE — Sistema de Gestão de Estoque

Resumo
-----
SGE é um sistema web para controle de estoque, entradas (inflows), saídas (outflows), fornecedores, marcas e categorias, usando Django + Django REST Framework. O projeto contém interface web com templates e API JWT para integração.


Tecnologias
-----------
- Python + Django 6.x
- Django REST Framework + Simple JWT
- drf-yasg (documentação Swagger/Redoc)
- Bootstrap + Chart.js no frontend
- SQLite (desenvolvimento)


API (JWT)
---------
- Endpoints de autenticação JWT: [`authentication/urls.py`](authentication/urls.py) — `/api/v1/token/`, `/api/v1/token/refresh/`, `/api/v1/token/verify/`.
- Documentação automática: [`documentation/urls.py`](documentation/urls.py) — `/api/v1/swagger/`, `/api/v1/redoc/`.

Permissões e administração
--------------------------
- Views usam `PermissionRequiredMixin` e permissões de modelo (ex.: `brands.view_brand`, `outflows.view_outflow`). Veja exemplos em [brands/views.py](brands/views.py) e [outflows/views.py](outflows/views.py).
- Painel admin padrão do Django disponível em `/admin/`.


Boas práticas
------------
- Não versionar credenciais (ex.: `senha.txt` deve ser removido do repositório).
- Mantenha DEBUG= False em produção e configure ALLOWED_HOSTS em [`app.settings`](app/settings.py).

Testes
------
- Estrutura de testes por app (ex.: [brands/tests.py](brands/tests.py)). Rodar:
  ```sh
  python manage.py test
  ```

Contribuição
------------
- Fork + branch por feature + PR.
- Siga lint (flake8) e escreva testes para novas funcionalidades.


Contato / Observações
---------------------
- Para comportamento das métricas e dashboards veja [`app.metrics`](app/metrics.py) — [app/metrics.py](app/metrics.py).
- Para rotas e views específicas veja [app/urls.py](app/urls.py) e os arquivos de views listados acima.