from fastapi import  FastAPI

import controllers.restaurant_ratings

app = FastAPI()

app.include_router(controllers.restaurant_ratings.router)