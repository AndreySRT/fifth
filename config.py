import os                       # os - вроде как модуль операционной системы
from dotenv import load_dotenv  # Здесь по легче,
                                # из модуля dotenv импортируется его функция load_dotenv

load_dotenv()

telegram_token = os.getenv('api_key') 