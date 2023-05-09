# PlaceKG 
: 코스추천을 위한 지역별 장소의 특성을 담은 지식그래프
  - 상호명과 주소 정보가 담긴 장소를 behavior(eat,drink,walk,see,play)로 구분
  - 서울의 행정동과 장소의 주소정보를 비교해 장소와 지역을 연결
  - 위의 정보를 담은 RDF 파일 생성 
  
  # DATA 
  - data set
    1.  store__info.csv : https://www.dropbox.com/sh/1u8jy3zk3788w6m/AABGAbAI2P1Bp8AhWRhowPEha?dl=0
         - 대분류소분류 속성정리표 (store__info.csv에 참고 사용) : https://www.dropbox.com/s/jranoz02djjxnjg/%EB%8C%80%EB%B6%84%EB%A5%98%EC%86%8C%EB%B6%84%EB%A5%98%20%EC%86%8D%EC%84%B1%EC%A0%95%EB%A6%AC%ED%91%9C.xlsx?dl=0
         
            ![image](https://user-images.githubusercontent.com/84067454/237025186-8a1dd293-519d-48be-8362-d14ba200b8b8.png)

    2.  행정동_법정동_20230330.csv : https://www.dropbox.com/s/vkmyrni5efhibtx/%ED%96%89%EC%A0%95%EB%8F%99_%EB%B2%95%EC%A0%95%EB%8F%99_20230330.csv?dl=0
 
 # KnowledgeGraph
  - Ontotext GraphDB ( based on this program )
  - PlaceKG example
    1. 교남동 푸하하크림빵
        - http://localhost:7200/graphs-visualizations?saved=c94917e54051474db17796805fd47344
            ![image](https://github.com/seojungin/PlaceKG/assets/84067454/be11d83c-525a-4941-9a8c-99199567d7c1)
    2. 연남동 대분류 (eat,drink,walk,see,play) 에 따른 장소 (지역에 따른 장소 분류) 
        - http://localhost:7200/graphs-visualizations?saved=9ab37e2922eb47eab1fd69e364d53485
            ![image](https://github.com/seojungin/PlaceKG/assets/84067454/e96b8578-4790-41ff-b12d-cd3c8b93080e)

  - PlaceKG SPARQL Query example
    1. 장소의 상호명 검색 
        - Query : select * where { ?s <http://Place.com/place/name> ?name. } 
        - Query example
            ![image](https://github.com/seojungin/PlaceKG/assets/84067454/21c2b056-a9d8-43ae-afca-c4e36683637b)

