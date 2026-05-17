from fastapi import FastAPI
from routers import delete_request,update_request 
from routers import post_request,normal_get_request,understanding_http_expection,get_path_query_validation_request


app = FastAPI()
app.include_router(delete_request.router)
app.include_router(post_request.router)
app.include_router(post_request.router)
app.include_router(normal_get_request.router)
app.include_router(understanding_http_expection.router)
app.include_router(get_path_query_validation_request.router)
app.include_router(update_request.router)
