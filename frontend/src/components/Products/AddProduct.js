import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { createProduct } from '../../services/products';

const AddProduct = () => {
  const history = useHistory();
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createProduct(formData);
    history.push('/');
  };

  return (
    <div>
      <h1>Add Product</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input type="text" name="name" onChange={handleChange} />
        </div>
        <div>
          <label>Description:</label>
          <input type="text" name="description" onChange={handleChange} />
        </div>
        <div>
          <label>Price:</label>
          <input type="number" name="price" onChange={handleChange} />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AddProduct;