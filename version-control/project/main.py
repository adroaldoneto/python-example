import uvicorn

from controller import router
from project import app

app.include_router(router)


# Adicione o código para importar os arquivos de modelo, usecase e view
# e para configurar as rotas da sua aplicação


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

