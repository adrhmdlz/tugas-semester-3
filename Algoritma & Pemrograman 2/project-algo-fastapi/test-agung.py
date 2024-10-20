from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Ujicoba (BaseModel):
    a: int
    b: int
    oprator : str


soal1Data = [] #sebagai aray atau penampung dari semua req atau data
 
@app.post("/soal1")
def data (request : Ujicoba):
    soal1Data.append({"data":request})
    
# jiak membuat fungi atau fariable yang namanya 
# lebih dari 1 kata kata ke dua dan seterusnya di awali dengan huruf kapital(camel case)
@app.get("/soal1")
def getSoal1 ():
    for dataSoal in soal1Data:
      if dataSoal["data"].oprator == '+':
          c = dataSoal["data"].a + dataSoal["data"].b 
      elif dataSoal["data"].oprator == '*':
          c = dataSoal["data"].a * dataSoal["data"].b
    
    return{
        "data": f"{dataSoal["data"].a} {dataSoal["data"].oprator} {dataSoal["data"].b} = {c}"
    }