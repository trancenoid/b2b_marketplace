from app.database import crud
from app.schemas import UserRegistration, PasswordReset
from passlib.context import CryptContext
from datetime import timedelta
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_MINUTES = 15

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def register_user(db, user_registration: UserRegistration):
    hashed_password = get_password_hash(user_registration.password)
    return crud.create_user(db, username=user_registration.username,
                            password=hashed_password,
                            business_name=user_registration.business_name,
                            email=user_registration.email,
                            phone_number=user_registration.phone_number,
                            business_category_id=user_registration.business_category_id)

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