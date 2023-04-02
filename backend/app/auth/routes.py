from fastapi import APIRouter, Depends
from app.schemas import UserLogin, UserRegistration, PasswordReset
from .utils import *
from datetime import timedelta
import datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.database.session import SessionLocal, get_session
from app.database import crud
from app.database.models import User
from app.schemas import TokenData
from sqlalchemy.orm import Session

auth_router = APIRouter()

# JWT token related constants
SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict, expires_delta: timedelta = None):
    # creates 
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise CredentialsException()
        token_data = TokenData(username=username)
    except JWTError:
        raise CredentialsException()
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise CredentialsException()
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise InvalidCredentialsException()
    return current_user

@auth_router.post("/register")
async def register(user_registration: UserRegistration, db: Session = Depends(get_session)):
    """
    Registers a new user with the provided details.
    """
    return await register_user(db, user_registration)

@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    """
    Authenticates the user with the provided credentials and returns a JWT token.
    """
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user:
        raise InvalidCredentialsException()
    if not verify_password(form_data.password, user.password):
        raise InvalidCredentialsException()
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post("/reset-password")
async def reset_password_request(password_reset: PasswordReset, db: Session = Depends(get_session)):
    """
    Sends an email to the user with a password reset link.
    """
    return reset_password(db, password_reset)
