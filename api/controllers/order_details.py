from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

# order_details table wants
    # order_id, sandwich_id, price, recipes, description

#CREATE
def create(db: Session, order_details):
    # Create a new instance of the order_details model with the provided data
    db_order_details = models.OrderDetail(
        amount=order_details.amount,
        order_id=order_details.order_id,
        sandwich_id=order_details.sandwich_id

    )
    # Add the newly created order details object to the database session
    db.add(db_order_details)
    # Commit the changes to the database
    db.commit()
    # Refresh the order_details object to ensure it reflects the current state in the database
    db.refresh(db_order_details)
    # Return the newly created order_details object
    return db_order_details

#UPDATE
def update(db: Session, order_details, order_detail_id):
    # Query the database for the specific order to update -----> here we compare the primary key of order_details
    # with OrderDetail
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    # Extract the update data from the provided 'order_details' object
    update_data = order_details.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_order_details.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order details record
    return db_order_details.first()

#DELETE
def delete(db: Session, order_detail_id):
    #Query the database for the order_details to delete
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    # Delete the database record without synchronizing the session
    db_order_details.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#READ ALL
def read_all(db: Session):
    return db.query(models.OrderDetail).all()

#READ ONE
def read_one(db: Session, order_details, ):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details).first()
