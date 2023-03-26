from fastapi import Depends, FastAPI, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from utils.schemas import UserCreate,UserLogin
from sqlalchemy.sql import text
from database.models import Buyer,Seller
from database import get_db
from sqlalchemy.orm import Session
# Define the authentication configuration
JWT_SECRET_KEY = "your-secret-key"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 30

# Define the password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Define the FastAPI router
auth_router = APIRouter()

# Define the authentication functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return username

# Define the authentication routes
@auth_router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    if user.usertype == 'Buyer':
        user_obj = db.query(Buyer).filter(Buyer.username == user.username).first()
    elif user.usertype == 'Seller':
        user_obj = db.query(Seller).filter(Seller.username == user.username).first()
    else:
        raise HTTPException(status_code=400, detail="Invalid user type")

    if not user_obj:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not pwd_context.verify(user.password, user_obj.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    
    access_token_expires = timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    access_token = create_access_token(data={"sub": user_obj.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

# Define a protected endpoint
@auth_router.get("/users/me")
async def read_users_me(db = Depends(get_db), username: str = Depends(get_current_user)):
    user = db.execute(text("SELECT * FROM users WHERE username = ?"), [(username,)]).fetchone()
    return {"username": user["username"], "email": user["email"], "full_name": user["full_name"]}

@auth_router.post("/users")
async def create_user(user: UserCreate, db=Depends(get_db)):
    
    if user.usertype == 'Buyer':
        new_user = Buyer(business_name=user.business_name,
                         email=user.email,
                         phone_number=user.phone_number,
                         business_category=user.business_category,
                         username=user.username,
                         hashed_password=pwd_context.hash(user.password))
    else:
        new_user = Seller(business_name=user.business_name,
                          email=user.email,
                          phone_number=user.phone_number,
                          business_category=user.business_category,
                          username=user.username,
                          hashed_password=pwd_context.hash(user.password))

    # Check if the user already exists
    if db.query(type(new_user)).filter_by(username=new_user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    # Insert the user into the database
    db.add(new_user)
    db.commit()

    return {"message": "User created successfully"}