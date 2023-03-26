import React, { useState, useEffect } from 'react';
import Product from '../components/Products/Product';
import productsAPI from '../services/products';

const HomeScreen = () => {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    const fetchProducts = async () => {
      const data = await productsAPI.getProducts();
      setProducts(data);
    };
    fetchProducts();
  }, []);

  const filteredProducts = products.filter((product) =>
    product.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <input
        type='text'
        placeholder='Search Products'
        onChange={(e) => setSearch(e.target.value)}
      />
      <div className='product-list'>
        {filteredProducts.map((product) => (
          <Product key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
};

export default HomeScreen;