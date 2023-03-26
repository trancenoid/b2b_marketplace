import React, { useEffect, useState } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import { getProduct, updateProduct } from '../../services/products';

const EditProduct = () => {
  const { id } = useParams();
  const history = useHistory();
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
  });

  useEffect(() => {
    const fetchProduct = async () => {
      const product = await getProduct(id);
      setFormData({
        name: product.name,
        description: product.description,
        price: product.price,
      });
    };
    fetchProduct();
  }, [id]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await updateProduct(id, formData);
    history.push('/');
  };

  return (
    <div>
      <h1>Edit Product</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input type="text" name="name" value={formData.name} onChange={handleChange} />
        </div>
        <div>
          <label>Description:</label>
          <input type="text" name="description" value={formData.description} onChange={handleChange} />
        </div>
        <div>
          <label>Price:</label>
          <input type="number" name="price" value={formData.price} onChange={handleChange} />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default EditProduct;