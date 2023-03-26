import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

const Product = ({ product }) => {
  return (
    <View>
      <Text style={styles.productName}>{product.name}</Text>
      <Text>{product.description}</Text>
      <Text>Price: {product.price}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  productName: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
});

export default Product;