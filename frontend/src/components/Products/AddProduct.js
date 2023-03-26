import React, { useState } from "react";
import { View, Text, TextInput, Button } from "react-native";
import { createProduct } from "../../services/products";

const AddProduct = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    const data = new FormData();
    data.append("name", name);
    data.append("description", description);
    data.append("price", price);
    data.append("image", image);
    try {
      await createProduct(data);
      // history.push("/");
    } catch (error) {
      console.log(error);
      setLoading(false);
    }
  };

  return (
    <View>
      <Text>Add Product</Text>
      <TextInput
        placeholder="Name"
        value={name}
        onChangeText={(text) => setName(text)}
        required
      />
      <TextInput
        placeholder="Description"
        value={description}
        onChangeText={(text) => setDescription(text)}
        required
      />
      <TextInput
        placeholder="Price"
        value={price}
        onChangeText={(text) => setPrice(text)}
        keyboardType="numeric"
        required
      />
      <Button
        title="Choose Image"
        onPress={() => {
          // TODO: Add code to pick image
        }}
      />
      <Button
        title={loading ? "Adding..." : "Add"}
        onPress={handleSubmit}
        disabled={loading}
      />
    </View>
  );
};

export default AddProduct;