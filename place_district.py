from rdflib import Graph, URIRef, Literal
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD 
from rdflib import Graph, BNode
import pandas as pd
from rdflib import Namespace
import math

seoul_csv = pd.read_csv('./Plcae_KG/store_info.csv',encoding = 'cp949')
seoul_dong_csv = pd.read_csv('./Plcae_KG/district/행정동_법정동_20230330.csv',encoding = 'cp949')
seoul_dong_csv = seoul_dong_csv.loc[(seoul_dong_csv['시도명']=="서울특별시")]
dong_url = ''


dong_list=[]
def district_split():
    # 서울특별시에 존재 하는 동추출 
    for i, address in enumerate(seoul_dong_csv['읍면동명']):
        dong_list.append(address)
        new_dong_list = [x for x in dong_list if pd.isnull(x) == False]
    return new_dong_list

def data_disrict_split(address,f_dong_list):
    # 상권주소에서 동 추출 

    dong=address.split(" ",4)
    dong=dong[2].replace("동","")
    matching = []
    matching = [s for s in f_dong_list if dong in s] 
    
    return matching


