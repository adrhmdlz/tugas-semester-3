from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Biodata(BaseModel):
    nama: str
    tahun: int

biodataMahasiswa = []
biodataId = 0

@app.post('/soal-1')
async def post_soal_1(request: Biodata):
    global biodataId

    biodataId += 1
    biodataMahasiswa.append({ "id": biodataId, "data": request })
    print(biodataMahasiswa)


    return {
        "code": 200,
        "message": f"data dengan id {biodataId} berhasil dikirim!"
    }

@app.get("/soal-1")
def get_soal_1(id: int):
    for biodata in biodataMahasiswa:
        if biodata["id"] == id:
            return {
                "code": 200,
                "data": f"{biodata["data"].nama} adalah mahasiswa tahun {biodata["data"].tahun}"
            }

    return None

class Calculator(BaseModel):
    a: int
    b: int
    operator: str

calculatorData = []
calculatorId = 0

@app.post('/soal-2')
async def post_soal_2(request: Calculator):
    global calculatorId

    calculatorId += 1
    calculatorData.append({ "id": calculatorId, "data": request })
    
    return {
        "code": 200,
        "message": f"data dengan id {calculatorId} berhasil dikirim!"
    }

@app.get('/soal-2a')
def get_soal_2a(id: int):
    for calculator in calculatorData:
        if calculator["id"] == id:
            if (calculator["data"].operator == "+"):
                c = calculator["data"].a + calculator["data"].b
                opt = "tambah"
            elif (calculator["data"].operator == "-"):
                c = calculator["data"].a - calculator["data"].b
                opt = "kurang"
            elif (calculator["data"].operator == "*"):
                c = calculator["data"].a * calculator["data"].b
                opt = "kali"
            elif (calculator["data"].operator == "/"):
                c = calculator["data"].a / calculator["data"].b
                opt = "bagi"
            else:
                return None

            return {
                "status": 200,
                "msg": "success",
                "data": {
                    "a": calculator["data"].a,
                    "b": calculator["data"].b,
                    "operator": calculator["data"].operator,
                    "hasil": f"{calculator["data"].a} di{opt} {calculator["data"].b} sama dengan {c}"
                }
            }
    
    return None

@app.get('/soal-2b')
def get_soal_2b(id: int):
    for calculator in calculatorData:
        if calculator["id"] == id:
            match calculator["data"].operator:
                case "+":
                    c = calculator["data"].a + calculator["data"].b
                    opt = "tambah"
                case "-":
                    c = calculator["data"].a - calculator["data"].b
                    opt = "kurang"
                case "*":
                    c = calculator["data"].a * calculator["data"].b
                    opt = "kali"
                case "/":
                    c = calculator["data"].a / calculator["data"].b
                    opt = "bagi"
                case _:
                    return None

            return {
                "status": 200,
                "msg": "success",
                "data": {
                    "a": calculator["data"].a,
                    "b": calculator["data"].b,
                    "operator": calculator["data"].operator,
                    "hasil": f"{calculator["data"].a} di{opt} {calculator["data"].b} sama dengan {c}"
                }
            }

@app.get("/soal-2c")
def get_soal_2c(id: int):
    for calculator in calculatorData:
        if calculator["id"] == id:
            c = calculator["data"].a + calculator["data"].b if calculator["data"].operator == "+" else \
                calculator["data"].a - calculator["data"].b if calculator["data"].operator == "-" else \
                calculator["data"].a * calculator["data"].b if calculator["data"].operator == "*" else \
                calculator["data"].a / calculator["data"].b if calculator["data"].operator == "/" else None

            return {
                "status": 200,
                "msg": "success",
                "data": {
                    "a": calculator["data"].a,
                    "b": calculator["data"].b,
                    "operator": calculator["data"].operator,
                    "hasil": f"{calculator["data"].a} {calculator["data"].operator} {calculator["data"].b} = {c}"
                }
            }

class AgeCounter(BaseModel):
    tahunSekarang: int
    tahunLahir: int
    bulanSekarang: str
    bulanLahir: str

ageCounterData = []
ageCounterId = 0

@app.post("/soal-3")
async def post_soal_3(request: AgeCounter):
    global ageCounterId

    ageCounterId += 1
    ageCounterData.append({ "id": ageCounterId, "data": request })

    return {
        "code": 200,
        "message": f"data dengan id {ageCounterId} berhasil dikirim!"
    }

@app.get("/soal-3a")
def get_soal_3a(id: int):
    for ageData in ageCounterData:
        if ageData["id"] == id:
            months = ['januari', 'februari', 'maret', 'april', 'mei', 'juni', 'juli', 'agustus', 'september', 'oktober', 'november', 'desember']
            currentAge = ageData["data"].tahunSekarang - ageData["data"].tahunLahir

            for i in range(len(months)):
                if ageData["data"].bulanSekarang.lower() == months[i]:
                    currentMonth = i + 1
                if ageData["data"].bulanLahir.lower() == months[i]:
                    birthMonth = i + 1

            monthGap = currentMonth - birthMonth

            if monthGap < 0:
                currentAge -= 1
                monthGap += 12

            if monthGap == 0:
                data = f"Umur anda {currentAge} tahun"
            else:
                data = f"Umur anda {currentAge} tahun {monthGap} bulan"

            return {
                "code": 200,
                "message": "success",
                "data": data
            }

    return None

@app.get("/soal-3b")
def get_soal_3b(id: int):
    for ageData in ageCounterData:
        if ageData["id"] == id:
            months = ['januari', 'februari', 'maret', 'april', 'mei', 'juni',
                    'juli', 'agustus', 'september', 'oktober', 'november', 'desember']
            currentAge = ageData["data"].tahunSekarang - ageData["data"].tahunLahir

            i = 0
            while i < len(months):
                if ageData["data"].bulanSekarang.lower() == months[i]:
                    currentMonth = i + 1
                if ageData["data"].bulanLahir.lower() == months[i]:
                    birthMonth = i + 1
                i += 1

            monthGap = currentMonth - birthMonth

            if monthGap < 0:
                currentAge -= 1
                monthGap += 12

            if monthGap == 0:
                data = f"Umur anda {currentAge} tahun"
            else:
                data = f"Umur anda {currentAge} tahun {monthGap} bulan"

            return {
                "code": 200,
                "message": "success",
                "data": data
            }

    return None


@app.get("/soal-3c")
def get_soal_3c(id: int):
    for ageData in ageCounterData:
        if ageData["id"] == id:
            months = ['januari', 'februari', 'maret', 'april', 'mei', 'juni',
                    'juli', 'agustus', 'september', 'oktober', 'november', 'desember']
            currentAge = ageData["data"].tahunSekarang - ageData["data"].tahunLahir

            for index, month in enumerate(months):
                if ageData["data"].bulanSekarang.lower() == month:
                    currentMonth = index + 1
                if ageData["data"].bulanLahir.lower() == month:
                    birthMonth = index + 1

            monthGap = currentMonth - birthMonth

            if monthGap < 0:
                currentAge -= 1
                monthGap += 12

            if monthGap == 0:
                data = f"Umur anda {currentAge} tahun"
            else:
                data = f"Umur anda {currentAge} tahun {monthGap} bulan"

            return {
                "code": 200,
                "message": "success",
                "data": data
            }
