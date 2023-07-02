from datetime import datetime
import requests

filiais = {}
ids = []
nomes_filiais = []
csvs_filial = []
hora_data = datetime.now()
mes_ano = hora_data.strftime("%Y-%m")
ultima_data = mes_ano + '-01'

filiais_request = requests.get("https://project-482087131936180168.firebaseio.com/filiais/.json").json()
