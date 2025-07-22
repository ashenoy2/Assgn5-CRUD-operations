from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, order_details, sandwiches, recipes, resources

from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






#order table endpoints
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)





#order_details endpoints
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["OrderDetail"])
def create_order_details(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order_details=order_detail)

@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["OrderDetail"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@app.get("/order_details/{order_id}", response_model=schemas.OrderDetail, tags=["OrderDetail"])
def read_one_order_details(order_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, order_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="order details found")
    return order_detail


@app.put("/order_details/{order_id}", response_model=schemas.OrderDetail, tags=["OrderDetail"])
def update_one_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    existing_detail = order_details.read_one(db, order_detail_id)
    if existing_detail is None:
        raise HTTPException(status_code=404, detail="order details not found")
    return order_details.update(db=db, order_details=order_detail, order_detail_id = order_detail_id)


@app.delete("/order_details/{order_id}", tags=["OrderDetail"])
def delete_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    existing_detail = order_details.read_one(db, order_detail_id)
    if existing_detail is None:
        raise HTTPException(status_code=404, detail="order details not found")
    return order_details.delete(db=db , order_detail_id = order_detail_id)






#sandwiches.py endpoints
@app.post("/sandwich/", response_model=schemas.Sandwich, tags=["Sandwich"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db, sandwich)

@app.get("/sandwich/", response_model=list[schemas.Sandwich], tags=["Sandwich"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwich/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwich"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="sandwich not found")
    return sandwich

@app.put("/sandwich/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwich"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="sandwich not found")
    return sandwiches.update(db=db, sandwich=sandwich,sandwich_id=sandwich_id)

@app.delete("/sandwich/{sandwich_id}", tags=["Sandwich"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="sandwich not found")
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)






#recipes endpoints
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipe"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipe=recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipe"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipe"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipe"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="recipe not found")
    return recipes.update(db=db, recipe=recipe, recipe_id=recipe_id)

@app.delete("/recipes/{recipe_id}", tags=["Recipe"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="recipe not found")
    return recipes.delete(db=db, recipe_id=recipe_id)






#resources endpoints
@app.post("/resources/", response_model=schemas.Resource, tags=["Resource"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)


@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resource"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)


@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resource"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource


@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resource"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resources.read_one(db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="resource not found")
    return resources.update(db=db, resource=resource, resource_id=resource_id)


@app.delete("/resources/{resource_id}", tags=["Resource"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.delete(db=db, resource_id=resource_id)