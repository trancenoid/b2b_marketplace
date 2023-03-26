import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import { register } from '../../services/auth';

const Register = () => {
  const [businessName, setBusinessName] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [businessCategory, setBusinessCategory] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async () => {
    const user = await register(businessName, email, phoneNumber, businessCategory, password);
    // Do something with the user, such as storing it in local storage or state
  };

  return (
    <View>
      <Text>Business Name:</Text>
      <TextInput value={businessName} onChangeText={setBusinessName} />
      <Text>Email:</Text>
      <TextInput value={email} onChangeText={setEmail} />
      <Text>Phone Number:</Text>
      <TextInput value={phoneNumber} onChangeText={setPhoneNumber} />
      <Text>Business Category:</Text>
      <TextInput value={businessCategory} onChangeText={setBusinessCategory} />
      <Text>Password:</Text>
      <TextInput secureTextEntry value={password} onChangeText={setPassword} />
      <Button title="Submit" onPress={handleSubmit} />
    </View>
  );
};

export default Register;