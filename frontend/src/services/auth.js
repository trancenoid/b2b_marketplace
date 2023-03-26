import axios from 'axios';
import { AsyncStorage } from 'react-native';

const BASE_URL = 'http://192.168.1.33:8000';

// Login user and get access token
export const login = async (username, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/auth/token`, {
      username: username,
      password: password,
      scope: 'openid',
      grant_type: 'password',
    });
    const accessToken = response.data.access_token;
    await AsyncStorage.setItem('accessToken', accessToken);
    return true;
  } catch (error) {
    console.error(error);
    return false;
  }
};

// Register new user
export const register = async (username, businessName, email, phoneNumber, businessCategory, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/users/`, {
      username: username,
      business_name: businessName,
      email: email,
      phone_number: phoneNumber,
      business_category: businessCategory,
      password: password,
    });
    return true;
  } catch (error) {
    console.error(error);
    return false;
  }
};

// Logout user and remove access token
export const logout = async () => {
  try {
    await AsyncStorage.removeItem('accessToken');
    return true;
  } catch (error) {
    console.error(error);
    return false;
  }
};

// Check if user is authenticated
export const isAuthenticated = async () => {
  const accessToken = await AsyncStorage.getItem('accessToken');
  if (accessToken) {
    return true;
  } else {
    return false;
  }
};

// Get access token for authenticated user
export const getAccessToken = async () => {
  const accessToken = await AsyncStorage.getItem('accessToken');
  return accessToken;
};

// Get current user details
export const getCurrentUser = async () => {
  const accessToken = await getAccessToken();
  const response = await axios.get(`${BASE_URL}/users/me`, {
    headers: { Authorization: `Bearer ${accessToken}` },
  });
  const currentUser = response.data;
  return currentUser;
};