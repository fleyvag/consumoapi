import requests

# def get_pokemons(url='https://pokeapi.co/api/v2/pokemon-form/',offset=0):
    
    
    # args={'offset':offset} if offset else {}
    # response=requests.get(url,params=args)
    # vacia=[]
    # if response.status_code==200:
    #     payload=response.json()
    #     results=payload.get('results',[])

    #     vacia=[]
    #     if results:
    #         for pokemon in results:
    #             name=pokemon['name']
    #             # print(name)
                

    #             vacia.append(name)
    # return vacia
#-----------------------------------


# def get_pokemons(url='https://pokeapi.co/api/v2/pokemon/'):
    
#     response=requests.get(url)
#     if response.status_code==200:
#         data=response.json()  
#         return data
# def getnamepokemon(data):
#     nombre=data.get('name',[])
#     print(nombre)
#     return nombre
# def getimgpoke(data):
#     getsprite=data.get('sprites',[])
#     getimg=getsprite.get('other',[])
#     getimgother=getimg.get('dream_world',[])
#     getfinalimg=getimgother.get('front_default',[])
#     print(getfinalimg)
#     return getfinalimg
    
# # def get_morepokemon
# getnamepokemon(get_pokemons())
# getimgpoke(get_pokemons())
#-----------------------------------







# def get_pokemons(id):
#     url=f'https://pokeapi.co/api/v2/pokemon/{id}'
#     response=requests.get(url)
#     if response.status_code==200:
#         data=response.json()
#         print(data)
#         return data
# def getnamepokemon(data):
#     nombre=data.get('name',[])
#     print(nombre)
#     return nombre
# def getimgpoke(data):
#     getsprite=data.get('sprites',[])
#     getimg=getsprite.get('other',[])
#     getimgother=getimg.get('dream_world',[])
#     getfinalimg=getimgother.get('front_default',[])
#     print(getfinalimg)
#     return getfinalimg
# getimgpoke(get_pokemons(1))

# getnamepokemon(get_pokemons(1))



#-----------------------------------------------------------------------
# def pokemondata(id):
#     url=f'https://pokeapi.co/api/v2/pokemon/{id}'
    
def getnamepokemon(id):
    url=f'https://pokeapi.co/api/v2/pokemon/{id}'
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
    nombre=data.get('name',[])
    getsprite=data.get('sprites',[])
    getimg=getsprite.get('other',[])
    getimgother=getimg.get('dream_world',[])
    imagen=getimgother.get('front_default',[])
    # datos={
    #     'nombre': nombre,
    #     'imagen' : imagen,
    # }
    datos=(nombre,imagen)
    return datos
    # return print(datos)



def regresar_lista_pokes():
    i=0
    listaname=[]
    listaimg=[] 
    for i in range(0,10):
        i=i+1
        lista=getnamepokemon(i)
        listaname.append(lista[0])
        listaimg.append(lista[1])
    data={
        'pokes': listaname,
        'sprites': listaimg
    }
        
    print(data)


regresar_lista_pokes()





