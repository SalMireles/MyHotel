from fastapi import APIRouter
from hotel.operations.customers import CustomerCreateData, CustomerUpdateData, create_customer, update_customer, read_all_customers, read_customers

router = APIRouter()


@router.get("/customers")
def api_read_all_customers():
    return read_all_customers()

@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int):
    return read_customers(customer_id)

@router.post("/customer")
def api_create_customer(customer: CustomerCreateData):
    return create_customer(customer)


@router.post("/customer/{customer_id}")
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    return update_customer(customer_id, customer)