import React, { useState, useEffect } from 'react';
import { Text, View, TextInput, Button, StyleSheet } from 'react-native';
import { useNavigation, useParams } from '@react-navigation/native';
import { getProduct, updateProduct } from '../../services/products';

const EditProduct = () => {
  const navigation = useNavigation();
  const { id } = useParams();
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

  const handleChange = (name, value) => {
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async () => {
    await updateProduct(id, formData);
    navigation.navigate('Home');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Edit Product</Text>
      <View style={styles.form}>
        <View style={styles.inputContainer}>
          <Text style={styles.label}>Name:</Text>
          <TextInput
            style={styles.input}
            name="name"
            value={formData.name}
            onChangeText={(value) => handleChange('name', value)}
          />
        </View>
        <View style={styles.inputContainer}>
          <Text style={styles.label}>Description:</Text>
          <TextInput
            style={styles.input}
            name="description"
            value={formData.description}
            onChangeText={(value) => handleChange('description', value)}
          />
        </View>
        <View style={styles.inputContainer}>
          <Text style={styles.label}>Price:</Text>
          <TextInput
            style={styles.input}
            name="price"
            value={formData.price.toString()}
            keyboardType="numeric"
            onChangeText={(value) => handleChange('price', value)}
          />
        </View>
        <Button title="Submit" onPress={handleSubmit} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  form: {
    width: '80%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  label: {
    marginRight: 10,
    fontSize: 18,
  },
  input: {
    borderWidth: 1,
    borderColor: '#333',
    padding: 5,
    fontSize: 18,
    borderRadius: 5,
    flex: 1,
  },
});

export default EditProduct;