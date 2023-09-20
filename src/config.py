import os

from dotenv import load_dotenv

load_dotenv()

USE_ROUNDED_CORDS = False
OPENWEATHER_URL = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}&"
        "appid=" + os.getenv("OPENWEATHER_API") + "&lang=ru&"
                                                  "units=metric"
)
