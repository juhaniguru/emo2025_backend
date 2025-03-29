from fastapi import APIRouter

from services.restaurants_service import RestaurantService

router = APIRouter(tags=["restaurant_ratings"], prefix="/api/restaurants")


@router.get("/ratings")
async def get_restaurants_ratings(service: RestaurantService):
    return service.get_restaurants_ratings()

@router.get("/{resid}")
async def get_restaurant_ratings(resid: int, service: RestaurantService):
    return service.get_restaurant(resid)


@router.get("/{resid}/ratings")
async def get_ratings_by_restaurant(resid: int, service: RestaurantService):
    return service.get_ratings_restaurant(resid)
