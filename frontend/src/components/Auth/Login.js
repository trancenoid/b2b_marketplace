import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import { login } from '../../services/auth';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async () => {
    const token = await login(email, password);
    // Do something with the token, such as storing it in local storage or state
  };

  return (
    <View>
      <Text>Email:</Text>
      <TextInput value={email} onChangeText={setEmail} />
      <Text>Password:</Text>
      <TextInput secureTextEntry value={password} onChangeText={setPassword} />
      <Button title="Submit" onPress={handleSubmit} />
    </View>
  );
};

export default Login;