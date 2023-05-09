from rdflib import Graph, URIRef, Literal
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL, RDF, RDFS, VOID, XMLNS, XSD 
from rdflib import Graph, BNode
import pandas as pd
from rdflib import Namespace
import sys
import place_district


g = Graph()

Base=Namespace("http://Place.com/")


#class 정의 
behavior=URIRef(Base+"behavior")
place=URIRef(Base+"place/")    

#objectproperty 정의 (먹기/마시기/놀기/보기/걷기)
hasPlace_eat=URIRef(Base+"has_place_eat")
g.add((hasPlace_eat,RDF.type, OWL.ObjectProperty))   

hasPlace_drink=URIRef(Base+"has_place_drink")
g.add((hasPlace_drink,RDF.type, OWL.ObjectProperty))

hasPlace_play=URIRef(Base+"has_place_play")
g.add((hasPlace_play,RDF.type, OWL.ObjectProperty))  

hasPlace_see=URIRef(Base+"has_place_see")
g.add((hasPlace_see,RDF.type, OWL.ObjectProperty))  

hasPlace_walk=URIRef(Base+"has_place_walk")
g.add((hasPlace_walk,RDF.type, OWL.ObjectProperty))      

objectproperty_hehavior=[hasPlace_eat,hasPlace_drink,hasPlace_play,hasPlace_see,hasPlace_walk]

hasPlace=URIRef(Base+"has_place")
g.add((hasPlace,RDF.type, OWL.ObjectProperty)) 

# 대분류 정의 (먹기/마시기/놀기/보기/걷기)
eat=URIRef(behavior+"/eat")
drink=URIRef(behavior+"/drink")
play=URIRef(behavior+"/play")
see=URIRef(behavior+"/see")
walk=URIRef(behavior+"/walk")

hehavior = [eat,drink,play,see,walk]
for i in hehavior:
  
    g.add((i,RDFS.subClassOf, behavior)) 

district=URIRef(Base+"district")   
#지역 서울 추가
seoul=URIRef(district+"/seoul")  
# 지역-서울 서브클래스 설정  
g.add((seoul,RDFS.subClassOf,district)) 
#서울안에 존재하는 동 추가 
# dong_list 와 서울을 연결 
f_dong_list = place_district.district_split()
for i, dong in enumerate(f_dong_list): 
    dong = str(dong)
    dong_url=URIRef(seoul+"/"+dong)
    g.add((dong_url, RDF.type, seoul))



seoul_csv = pd.read_csv('./Plcae_KG/store_info.csv',encoding = 'cp949')
cate=[10000000,1000000,100000,10000,1000]

k=0
for index, value in enumerate(cate):
    seoul_cate_csv = seoul_csv.loc[(seoul_csv['PREF_SN']== value)]
    for p_name, address in zip(seoul_cate_csv['STORE_NM'],seoul_cate_csv['STORE_ADDR']):
        # 장소 
        p_name_node = BNode()
        name_url=URIRef(place+p_name_node)
        g.add((name_url, RDF.type, place))

        store_name=URIRef(place+"name")  
        store_add=URIRef(place+"address")  
        
        # 속성 추가 = 장소의 상호명
        g.add((name_url, store_name, Literal(p_name,datatype=XSD.string)))
        # 속성 추가 = 장소의 주소 
        g.add((name_url, store_add, Literal(address,datatype=XSD.string)))
          
        matching = place_district.data_disrict_split(address,f_dong_list)
        if len(matching) > 0:
            g.add((name_url,hasPlace, seoul+"/"+matching[0]))


        if(k==index):
            g.add((name_url,hasPlace, hehavior[index]))  
           
    k = k+1  
 
  
file = open("./Plcae_KG/place_rdf.txt", "w")
file.write(g.serialize(format='turtle').decode('utf-8'))
