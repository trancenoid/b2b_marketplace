import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, TextInput, TouchableOpacity } from 'react-native';
import { login, register } from '../services/auth';
import AsyncStorage from '@react-native-async-storage/async-storage';

const AuthScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [businessName, setBusinessName] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [businessCategory, setBusinessCategory] = useState('');
  const [registrationPassword, setRegistrationPassword] = useState('');
  const [userType, setUserType] = useState('');
  const readData = async () => {
    try {
      const userType = await AsyncStorage.getItem("userType");
      setUserType(userType);
    } catch (e) {
      alert('Failed to fetch the input from storage');
      console.error(e);
    }};

  useEffect(() => {
      readData();
  }, []);

  const handleLogin = async () => {
    const success = await login(username, password, userType);
    if (success) {
      navigation.replace('Home');
    }
  };

  const handleRegister = async () => {
    const success = await register(
      username,
      businessName,
      email,
      phoneNumber,
      businessCategory,
      registrationPassword,
      userType
    );
    if (success) {
      navigation.replace('Home');
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.formContainer}>
        <TextInput
          style={styles.input}
          placeholder="Username"
          onChangeText={(text) => setUsername(text)}
          value={username}
          autoCapitalize="none"
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          onChangeText={(text) => setPassword(text)}
          value={password}
          secureTextEntry
        />
        <TouchableOpacity style={styles.button} onPress={handleLogin}>
          <Text style={styles.buttonText}>Login</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.formContainer}>
      <TextInput
          style={styles.input}
          placeholder="Username"
          onChangeText={(text) => setUsername(text)}
          value={username}
        />
        <TextInput
          style={styles.input}
          placeholder="Business Name"
          onChangeText={(text) => setBusinessName(text)}
          value={businessName}
        />
        <TextInput
          style={styles.input}
          placeholder="Email"
          onChangeText={(text) => setEmail(text)}
          value={email}
          autoCapitalize="none"
        />
        <TextInput
          style={styles.input}
          placeholder="Phone Number"
          onChangeText={(text) => setPhoneNumber(text)}
          value={phoneNumber}
          keyboardType="phone-pad"
        />
        <TextInput
          style={styles.input}
          placeholder="Business Category"
          onChangeText={(text) => setBusinessCategory(text)}
          value={businessCategory}
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          onChangeText={(text) => setRegistrationPassword(text)}
          value={registrationPassword}
          secureTextEntry
        />
        <TouchableOpacity style={styles.button} onPress={handleRegister}>
          <Text style={styles.buttonText}>Register</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 32,
  },
  inputContainer: {
    marginBottom: 16,
  },
  input: {
    width: 250,
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 5,
    padding: 8,
    marginBottom: 8,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: 250,
  },
  button: {
    width: 100,
    height: 40,
    borderRadius: 5,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#1a73e8',
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  error: {
    color: 'red',
    marginBottom: 16,
  },
});
export default AuthScreen;