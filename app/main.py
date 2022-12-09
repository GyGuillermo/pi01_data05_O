from fastapi import FastAPI


app = FastAPI()


# Get para obtener titulo de máxima duración según tipo de film (película/serie), por plataforma y por año
@app.get("/get_max_duration/")
async def get_max_duration(año:int,plataforma:str,unit_time:str):
    import sys
    import os
    import pandas as pd
    import numpy as np
    url ='/home/guille/Escritorio/PI01_DATA05/Analisis/df_plataformas_concatenadas.csv'
    df = pd.read_csv(url)
    df_plataforma = df.query("plataforma == @plataforma and release_year == @año and time_unit == @unit_time")
    maximo = df_plataforma['duration'].idxmax()
    fila = df_plataforma.loc[maximo]
    return(fila['title'])

# Get para obtener cantidad de películas y series (separado) por plataforma
@app.get("/get_count_plataform/")
async def count_plataforma(plataforma:str):
    df = pd.read_csv(url)
    df_plataforma = df.query("plataforma == @plataforma")
    contador = df_plataforma.type.value_counts(sort=True)
    return (plataforma,str(contador[0]),contador[1])

# Get para obtener cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo
@app.get("/get_listedin/")
async def get_listedin (plataforma:str,categoria:str):
    df = pd.read_csv(url)
    df_plataforma = df.query("plataforma == @plataforma")
    return len(df_plataforma[df_plataforma.listed_in.str.contains(categoria)])

# Get para obtener actor que más se repite según plataforma y año
@app.get("/get_actor/")
async def get_actor(plataforma:str,año:int):
    df = pd.read_csv(url)
    df_plataforma = df.query("plataforma == @plataforma and release_year == @año")
    new_df = pd.DataFrame(df_plataforma["cast"].str.split(',', expand=True).stack(), columns=["C1"])
    contador = new_df['C1'].value_counts()
    return (contador.index[0],contador[0])