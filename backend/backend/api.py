from projects.api import router as projects_router
from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("projects/", projects_router)
