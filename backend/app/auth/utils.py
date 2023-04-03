from app.database import crud
from app.schemas import PasswordReset
from passlib.context import CryptContext
from fastapi import HTTPException, status
from app.database import models


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_MINUTES = 15

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def register_user(user, db):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    if user.type.value == "buyer":
        db_user = models.Buyer(
            username=user.username,
            email=user.email,
            password=get_password_hash(user.password),
            full_name=user.full_name,
            type=user.type.value,
        )
    elif user.type.value == "seller":
        db_user = models.Seller(
            username=user.username,
            email=user.email,
            password=get_password_hash(user.password),
            full_name=user.full_name,
            type=user.type.value,
        )
    else:
        raise HTTPException(status_code=400, detail="Invalid user type")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# async def login_user(db, username: str, password: str):
#     user = crud.get_user_by_username(db, username=username)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
#     if not verify_password(password, user.password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
#     return {"access_token": access_token, "token_type": "bearer"}

async def reset_password(db, password_reset: PasswordReset):
    user = crud.get_user_by_email(db, email=password_reset.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found")
    # Code for sending password reset email
    # ...
    return {"detail": "Password reset email sent"}

class GenericHTTPException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

class InvalidCredentialsException(GenericHTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Invalid username or password")

class CredentialsException(GenericHTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Could not validate credentials")

class InactiveUserException(GenericHTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Inactive user")

class DuplicateEntryException(GenericHTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=409, detail=detail)

class ResourceNotFoundException(GenericHTTPException):
    def __init__(self, resource_name: str):
        super().__init__(status_code=404, detail=f"{resource_name} not found")