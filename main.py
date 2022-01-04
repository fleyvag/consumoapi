
# import requests
# if  __name__=='__main__':
#     url='https://www.google.com.pe'
#     response=requests.get(url)
# print(response)


#--------------------------------
# import requests
# if  __name__=='__main__':
#     url='https://www.google.com.pe'
#     response=requests.get(url)
#     if response.status_code==200:
#         print(response.content)
#----------------------
# import requests
# if  __name__=='__main__':
#     url='https://www.google.com.pe'
#     response=requests.get(url)
#     if response.status_code==200:
#         content=response.content
#         file=open('google.html','wb')
#         file.write(content)
#         file.close()
#------------------------
# import requests
# if  __name__=='__main__':
#     url='https://httpbin.org/get'
#     response=requests.get(url)
#     if response.status_code==200:
#         content=response.content
#         # file=open('contenido.txt','wb')
#         # file.write(content)
#         # file.close()
#         print(content)
#------------------------

#----------------------- prueba en pokeapi
# import requests
# if  __name__=='__main__':
#     url='https://pokeapi.co/api/v2/pokedex/20'
#     response=requests.get(url)
#     print(response.url)
#     if response.status_code==200:
#         content=response.content
#         file=open('1.txt','wb')
#         file.write(content)
#         file.close()
#         print(content)
#---------------------------
# import requests
# if  __name__=='__main__':
#     url='https://httpbin.org/get'
#     args={'nombre':'frank','curso':'python'}

#     response=requests.get(url,params=args)
#     print(response.url)

#     if response.status_code==200:
#         content=response.content
#         print(content)

#--------------------
# import requests
# import json 
# if  __name__=='__main__':
#     url='https://httpbin.org/get'
#     args={'nombre':'frank','curso':'python'}

#     response=requests.get(url,params=args)
#     # print(response.url)
    
#     if response.status_code==200:
#         #forma1
#         # respjson=response.json()#diccionario
#         # origin=respjson['origin']
#         # print(origin)

#         #--forma2 usando lib json
#         respjson=json.loads(response.text)
#         origin=respjson['origin']
#         print(origin)
# POST------------------------
import requests
import json 
if  __name__=='__main__':
    url='https://httpbin.org/post'
    args={'nombre':'frank','curso':'python'}

    response=requests.post(url,params=args)
    
    if response.status_code==200:
        print(response.content)