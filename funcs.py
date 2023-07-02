from variables import *
from generate_url_amazon import generateUrl
from treat_csv import treat_csv
from rank_products import rank_products

def main(id):
    url = generateUrl(int(id))
    csv = treat_csv(url['url'])
    csv = rank_products(csv, url['bucket'])