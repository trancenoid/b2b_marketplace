import axios from 'axios';

const BASE_URL = 'http://localhost:8000/';

const productAPI = {
  getAll: async () => {
    const response = await axios.get(`${BASE_URL}/products`);
    return response.data;
  },
  getOne: async (id) => {
    const response = await axios.get(`${BASE_URL}/products/${id}`);
    return response.data;
  },
  create: async (product) => {
    const response = await axios.post(`${BASE_URL}/products`, product);
    return response.data;
  },
  update: async (id, product) => {
    const response = await axios.put(`${BASE_URL}/products/${id}`, product);
    return response.data;
  },
  delete: async (id) => {
    const response = await axios.delete(`${BASE_URL}/products/${id}`);
    return response.data;
  },
};

export default productAPI;