import axios from "axios";

const BASE_URL = "http://192.168.1.33:8000/api/orders/";

const createOrder = async (orderData, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  try {
    const res = await axios.post(BASE_URL, orderData, config);
    return res.data;
  } catch (error) {
    console.error(error);
  }
};

const getActiveOrders = async (token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  try {
    const res = await axios.get(`${BASE_URL}?status=active`, config);
    return res.data;
  } catch (error) {
    console.error(error);
  }
};

const getCompletedOrders = async (token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  try {
    const res = await axios.get(`${BASE_URL}?status=completed`, config);
    return res.data;
  } catch (error) {
    console.error(error);
  }
};

const updateOrder = async (orderId, orderData, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  try {
    const res = await axios.put(`${BASE_URL}${orderId}`, orderData, config);
    return res.data;
  } catch (error) {
    console.error(error);
  }
};

const deleteOrder = async (orderId, token) => {
  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  try {
    await axios.delete(`${BASE_URL}${orderId}`, config);
  } catch (error) {
    console.error(error);
  }
};

export default {
  createOrder,
  getActiveOrders,
  getCompletedOrders,
  updateOrder,
  deleteOrder,
};