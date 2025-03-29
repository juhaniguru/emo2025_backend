from typing import Annotated

from fastapi import Depends

from repos.restaurants_repo import RestaurantRepo, init_restaurant_repo


class ResServ:
    def __init__(self, repo: RestaurantRepo):
        self.repo = repo

    def get_restaurants_ratings(self):
        return self.repo.get_ratings()

    def get_restaurant(self, _id):
        return self.repo.get_restaurant(_id)

    def get_ratings_restaurant(self, _id):
        return self.repo.get_ratings_by_restaurant(_id)


def init_restaurants_service(repo: RestaurantRepo = Depends(init_restaurant_repo)):
    return ResServ(repo)


RestaurantService = Annotated[ResServ, Depends(init_restaurants_service)]


