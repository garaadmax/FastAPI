import hashlib
from fastapi import APIRouter


router = APIRouter(
    prefix="/login",
    tags=["login"]
)

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# def router_login(username, password, stored_hash):
#     # Create a SHA-256 hash of the input password
#     password_hash = hashlib.sha256(password.encode()).hexdigest()
#     # Compare the generated hash with the stored hash
#     return password_hash == stored_hash