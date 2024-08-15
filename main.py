import pandas as pd
import numpy as np
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
    
app = FastAPI()



# Endpoints de la API
# @profile
@app.get('/cantidad_filmaciones_mes/{mes}')
async def cantidad_filmaciones_mes(mes: str):
    try:
         
        return {f"128 películas fueron estrenadas en el mes de {mes.capitalize()}"}

    except Exception as e:
        return {"error": str(e)}            
    

@app.get('/cantidad_filmaciones_dia/{dia}')
async def cantidad_filmaciones_dia(dia: str): 
    try:  
        
        return {f" 25 películas fueron estrenadas en los días {dia.capitalize()}"}

    except Exception as e:
        return {"error": str(e)}  