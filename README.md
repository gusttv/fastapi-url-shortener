# URL Shortener API

Esta é uma aplicação de encurtador de URLs construída com **FastAPI** e **SQLAlchemy**, utilizando o banco de dados SQLite. 

## 🚀 Funcionalidades

- **Criar URL encurtada**: Receba uma URL longa e gere uma versão encurtada.
- **Redirecionar para a URL original**: Use a URL encurtada para acessar o destino original.
- **Persistência**: As URLs são armazenadas em um banco SQLite.

## 📂 Estrutura do Projeto

```
project/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints.py      
│   ├── core/
│   │   ├── __init__.py
│   │   ├── logger.py       
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py    
│   ├── models/
│   │   ├── __init__.py
│   │   ├── url_model.py    
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── url_schema.py  
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── shortener.py    
│   └── main.py            
└── requirements.txt    
```    

Esse projeto foi desenvolvido como teste para estudos em [FastAPI](https://fastapi.tiangolo.com/).
