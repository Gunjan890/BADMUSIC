import json
import os

YOUTUBE = {
    "access_token": "ya29.a0AeDClZBIACc7kPPRpr6F1QS2W23FewZ7BUl4_RhJMNyuQPoDxAW4ZUmy1Joj71bg2hhCoOSy-8M-P9Dr3H71Iyd3Y3zV4muwvYClMlD4Yjbi_PBAIMajmPYt7Fd-3OUqTa10LkrjmSp8x8UtAy_Si84DxMHe_UQ4uBgNJgm487MXnyqbna_6aCgYKAbwSARASFQHGX2MifsiT-wpTFdqc1EBlhUHAFQ0187",
    "expires": 1730267664.803879,
    "token_type": "Bearer",
    "refresh_token": "1//05e_6MmGv8p13CgYIARAAGAUSNwF-L9IrQR-txkBUpPem86mSv2-5sLMahSswgSNeBa-pBdFlL_spq34l5WGD7Zoc3EbM6tatFVs"
}

def badmunda():
    TOKEN_DATA = os.getenv("TOKEN_DATA")
    if not TOKEN_DATA:
        os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
