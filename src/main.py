from fastapi import FastAPI,Request
from typing import Optional, Union
from pydantic import BaseModel
import os
import socket

app = FastAPI()

class Package(BaseModel):
    name: str
    number: float
    description: Optional[str] = None


@app.get("/")
async def helloWorld():
        return {"Hello":"world APP2"}
"""
@app.get("/item/{item_id}")
async def get_item(item_id:int):
    return {"item_id": item_id}

@app.get("/item/")
async def read_item(number:int,text: str):
        return {"number":number,"text":text} 
"""

@app.get("/IP/{item_id}")
def extract_ip(item_id: str):
    client_host = socket.gethostname()
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return {"client_name" :client_host,"client_ip": IP , "item_id": item_id ,"App":"App2"}