from variables import *

def generateUrl(filial_escolhida):
    
    # criando dict com nome, id, bucket name e region das filiais
    for item in filiais_request:
        bucket_name = filiais_request[item].get('s3', 'none')
        if bucket_name != 'none':
          region = bucket_name.get('region', 'none')
          bucket_name = bucket_name.get('bucket_name', 'none')
          filiais[filiais_request[item]['nome_fantasia']] = {'id':item, 'bucket_name':bucket_name, 'region':region}
        else:
          filiais[filiais_request[item]['nome_fantasia']] = {'id':item, 'bucket_name':'none', 'region':'none'}

    # criando e printando lista enumerada com todas as lojas
    for i,  item in enumerate(filiais):
      ids.append(filiais[item]['id'])
      nomes_filiais.append(item)

    # colocando tudo em váriavél
    filial_id = ids[int(filial_escolhida)]
    filial_nome = nomes_filiais[filial_escolhida]
    bucket = filiais[filial_nome]['bucket_name']
    region = filiais[filial_nome]['region']

    # request do csv mix
    csvs_filial_request = requests.get(f"https://project-482087131936180168.firebaseio.com/arquivos_csv/{filial_id}/{ultima_data}.json").json()

    for csvs in csvs_filial_request:
      csvs_filial.append(csvs)

    # encontrar o mix entre os csvs
    contador = -1
    rodando = True

    # loop até encontrar arquivo com 'mix' no nome
    while rodando:
      if 'mix' in csvs_filial[contador]:
        mix_filial = csvs_filial[contador]
        rodando = False
      else:
        contador = contador - 1
    print(f'FIND FILE: {mix_filial}')

    # montar link da amazon com o nome do arquivo mix
    if bucket != 'none' and region != 'none':
      urlAmazon = f"https://{bucket}.s3.{region}.amazonaws.com/{mix_filial}.csv"
    elif bucket != 'none':
      urlAmazon = f"https://{bucket}.s3.amazonaws.com/{mix_filial}.csv"
    else:
      print('ARQUIVO NÃO EXISTENTE')

    return {'url':urlAmazon, 'bucket':bucket, 'region':region}
