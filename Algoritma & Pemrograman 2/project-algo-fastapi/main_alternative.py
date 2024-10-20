from fastapi import FastAPI, Request
from fastapi.exception_handlers import JSONResponse

app = FastAPI()

class CustomAPIError(Exception):
    def __init__(self, statusCode: int, message: str):
        self.statusCode = statusCode
        self.message = message

@app.exception_handler(CustomAPIError)
async def query_parameter_error_handler(request: Request, exc: CustomAPIError):
    return JSONResponse(
        status_code=exc.statusCode,
        content={
            "code": exc.statusCode,
            "message": exc.message
        }
    )

@app.get('/soal-1')
def get_soal_1(nama: str, tahun: str):
    if not nama:
        raise CustomAPIError(
            400, "Query parameter 'nama' required and must be a string")

    try:
        tahun1 = int(tahun)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'tahun' required and must be a integer")

    return {
        "status": 200,
        "message": "success",
        "data": f"{nama} adalah mahasiswa angkatan {tahun1}"
    }


@app.get('/soal-2a')
def get_soal_2a(a: str, b: str, operator: str):
    try:
        number1 = int(a)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'a' required and must be a integer")

    try:
        number2 = int(b)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'b' required and must be a integer")

    if (operator == "+"):
        c = number1 + number2
        opt = "tambah"
    elif (operator == "-"):
        c = number1 - number2
        opt = "kurang"
    elif (operator == "*"):
        c = number1 * number2
        opt = "kali"
    elif (operator == "/"):
        c = number1 / number2
        opt = "bagi"
    else:
        raise CustomAPIError(404, "Operator not found")

    return {
        "status": 200,
        "msg": "success",
        "data": {
            "a": a,
            "b": b,
            "operator": operator,
            "hasil": f"{number1} di{opt} {number2} sama dengan {c}"
        }
    }


@app.get('/soal-2b')
def get_soal_2b(a: str, b: str, operator: str):
    try:
        number1 = int(a)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'a' required and must be a integer")

    try:
        number2 = int(b)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'b' required and must be a integer")

    match operator:
        case "+":
            c = number1 + number2
            opt = "tambah"
        case "-":
            c = number1 - number2
            opt = "kurang"
        case "*":
            c = number1 * number2
            opt = "kali"
        case "/":
            c = number1 / number2
            opt = "bagi"
        case _:
            raise CustomAPIError(404, "Operator not found")

    return {
        "status": 200,
        "msg": "success",
        "data": {
            "a": a,
            "b": b,
            "operator": operator,
            "hasil": f"{number1} di{opt} {number2} sama dengan {c}"
        }
    }


@app.get("/soal-2c")
def get_soal_2c(a: int, b: int, operator: str):
    try:
        number1 = int(a)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'a' required and must be a integer")

    try:
        number2 = int(b)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'b' required and must be a integer")

    c = a + b if operator == "+" else a - b if operator == "-" else a * \
        b if operator == "*" else a / b if operator == "/" else None

    if c == None:
        raise CustomAPIError(404, "Operator not found")

    return {
        "status": 200,
        "msg": "success",
        "data": {
            "a": a,
            "b": b,
            "operator": operator,
            "hasil": f"{number1} {operator} {number2} = {c}"
        }
    }


@app.get("/soal-3a")
def get_soal_3a(tahunSekarang: str, tahunLahir: str, bulanSekarang: str, bulanLahir: str):
    try:
        currentYear = int(tahunSekarang)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'tahunSekarang' required and must be a integer")

    try:
        birthYear = int(tahunLahir)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'tahunLahir' required and must be a integer")

    if not bulanSekarang:
        raise CustomAPIError(
            400, "Query parameter 'bulanSekarang' required and must be a string")

    if not bulanLahir:
        raise CustomAPIError(
            400, "Query parameter 'bulanLahir' required and must be a string")

    months = ['januari', 'februari', 'maret', 'april', 'mei', 'juni',
              'juli', 'agustus', 'september', 'oktober', 'november', 'desember']
    currentAge = currentYear - birthYear

    for i in range(len(months)):
        if bulanSekarang.lower() == months[i]:
            currentMonth = i + 1
        if bulanLahir.lower() == months[i]:
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


@app.get("/soal-3b")
def get_soal_3b(tahunSekarang: str, tahunLahir: str, bulanSekarang: str, bulanLahir: str):
    try:
        currentYear = int(tahunSekarang)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'tahunSekarang' required and must be a integer")

    try:
        birthYear = int(tahunLahir)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'tahunLahir' required and must be a integer")

    if not bulanSekarang:
        raise CustomAPIError(
            400, "Query parameter 'bulanSekarang' required and must be a string")

    if not bulanLahir:
        raise CustomAPIError(
            400, "Query parameter 'bulanLahir' required and must be a string")

    months = ['januari', 'februari', 'maret', 'april', 'mei', 'juni',
              'juli', 'agustus', 'september', 'oktober', 'november', 'desember']
    currentAge = currentYear - birthYear

    i = 0
    while i < len(months):
        if bulanSekarang.lower() == months[i]:
            currentMonth = i + 1
        if bulanLahir.lower() == months[i]:
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


@app.get("/soal-3c")
def get_soal_3c(tahunSekarang: str, tahunLahir: str, bulanSekarang: str, bulanLahir: str):
    try:
        currentYear = int(tahunSekarang)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'tahunSekarang' required and must be a integer")

    try:
        birthYear = int(tahunLahir)
    except ValueError:
        raise CustomAPIError(
            400, "Query parameter 'tahunLahir' required and must be a integer")

    if not bulanSekarang:
        raise CustomAPIError(
            400, "Query parameter 'bulanSekarang' required and must be a string")

    if not bulanLahir:
        raise CustomAPIError(
            400, "Query parameter 'bulanLahir' required and must be a string")

    months = ['januari', 'februari', 'maret', 'april', 'mei', 'juni',
              'juli', 'agustus', 'september', 'oktober', 'november', 'desember']
    currentAge = currentYear - birthYear

    for index, month in enumerate(months):
        if bulanSekarang.lower() == month:
            currentMonth = index + 1
        if bulanLahir.lower() == month:
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
