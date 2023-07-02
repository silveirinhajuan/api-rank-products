from typing import Union
from pathlib import Path

from fastapi import FastAPI, Response
from fastapi.responses import FileResponse

from generate_url_amazon import generateUrl
from treat_csv import treat_csv
from rank_products import rank_products

app = FastAPI()


@app.get("/{item_id}")
async def download_csv(item_id: int, response: Response):
    url = generateUrl(item_id)
    # Chama a função generaterURL para gerar o URL do CSV bruto
    csv = treat_csv(url['url'])

    # Chama a função rankCSV para realizar o ranqueamento dos produtos no CSV tratado
    csv = rank_products(csv, url['bucket'])
    print(csv)

    # Define o caminho completo para o arquivo CSV gerado
    csv_path = Path(__file__).parent / csv

    # Lê o conteúdo do arquivo CSV e retorna como resposta
    with open(csv_path, mode="rb") as file:
        csv_content = file.read()

    # Configura a resposta da API com o arquivo CSV
    response.headers["Content-Disposition"] = f"attachment; filename={csv}"
    response.headers["Content-Type"] = "text/csv"

    print(f'O nome do csv será: {csv}')

    return FileResponse(path=csv_path, media_type="text/csv", filename=csv)