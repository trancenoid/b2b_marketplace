import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const WelcomeScreen = ({ navigation }) => {
  const [userType, setUserType] = useState(null);

  const handleUserType = (type) => {
    AsyncStorage.setItem('userType', type);
    setUserType(type);
  };

  const handleLogin = () => {
    navigation.navigate('Auth');
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ fontSize: 24, fontWeight: 'bold' }}>Welcome to B2BMP</Text>
      <Text style={{ marginVertical: 20, fontSize: 18 }}>
        Are you a Buyer or a Seller?
      </Text>
      <View style={{ flexDirection: 'row' }}>
        <Button title="Buyer" onPress={() => handleUserType('Buyer')} />
        <Button title="Seller" onPress={() => handleUserType('Seller')} />
      </View>
      {userType && (
        <Button title="Login" onPress={handleLogin} style={{ marginTop: 20 }} />
      )}
    </View>
  );
};

export default WelcomeScreen;