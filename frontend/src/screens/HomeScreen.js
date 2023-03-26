import React, { useState, useEffect } from 'react';
import Product from '../components/Products/Product';
import productsAPI from '../services/products';
import { View, TextInput, FlatList } from 'react-native';

const HomeScreen = () => {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    const fetchProducts = async () => {
      const data = await productsAPI.getAll();
      setProducts(data);
    };
    fetchProducts();
  }, []);

  const filteredProducts = products.filter((product) =>
    product.name.toLowerCase().includes(search.toLowerCase())
  );

  const renderItem = ({ item }) => (
    <Product key={item.id} product={item} />
  );

  return (
    <View>
      <TextInput
        placeholder='Search Products'
        onChangeText={(text) => setSearch(text)}
      />
      <FlatList
        data={filteredProducts}
        renderItem={renderItem}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

export default HomeScreen;