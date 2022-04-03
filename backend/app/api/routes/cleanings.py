from typing import List

from fastapi import APIRouter

# router - маршрутизатор
router = APIRouter()

# декоратор задает метод запроса (отправки сигнала по маршруту)
@router.get('/')
# asyns def  создает подпрограмму
async def get_all_cleanings() -> List[dict]:
        cleanings = [
        {"id": 1, "name": "My house", "cleaning_type": "full_clean", "price_per_hour": 29.99},
        {"id": 2, "name": "Someone else's house", "cleaning_type": "spot_clean", "price_per_hour": 19.99}
    ]
        return cleanings
